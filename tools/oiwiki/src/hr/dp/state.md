---
title: DP s bitmaskama
---

## Uvod

DP s bitmaskama (bitmask DP, DP sa sažimanjem stanja) vrsta je dinamičkog programiranja u kojoj se skup stanja pretvara u cijeli broj koji se zapisuje u DP stanje, čime se omogućuju prijelazi stanja.

Za manju vremensku složenost obično treba tražiti stanja s manjim brojem mogućih vrijednosti. U većini zadataka koriste se binarna stanja: $n$-bitnim binarnim brojem prikazuje se $n$ nezavisnih binarnih stanja.

Sažimanje stanja obično uključuje bitovne operacije; o osnovnim bitovnim operacijama vidi stranicu [Bitovne operacije](../math/bit.md).

## Primjer 1

???+ note "[„SCOI2005” Kraljevi koji se ne napadaju](https://loj.ac/problem/2153)"
    Na šahovsku ploču $N\times N$ treba postaviti $K$ kraljeva ($1 \leq N \leq 9, 1 \leq K \leq N \times N$) tako da se međusobno ne napadaju. Koliko ima načina postavljanja?
    
    Kralj napada po jedno susjedno polje gore, dolje, lijevo, desno te gore-lijevo, dolje-lijevo, gore-desno i dolje-desno, ukupno $8$ polja.

### Objašnjenje

Neka $f(i,j,l)$ označava broj valjanih rasporeda u prvih $i$ redaka, u kojima je stanje $i$-tog retka $j$ i na ploči je već postavljeno $l$ kraljeva.

Za stanje s rednim brojem $j$ raspored kraljeva prikazujemo binarnim brojem $sit(j)$: ako je neki bit broja $sit(j)$ jednak $0$, na odgovarajućem položaju nema kralja, a ako je $1$, ondje jest kralj; $sta(j)$ označava broj kraljeva u tom stanju, tj. broj znamenaka $1$ u binarnom broju $sit(j)$. Primjerice, stanje na slici dolje prikazuje se binarnim brojem $100101$ (lijeva strana ploče odgovara nižim bitovima), pa je $sit(j)=100101_{(2)}=37, sta(j)=3$.

![](./images/SCOI2005-互不侵犯.png)

Neka je stanje trenutnog retka $j$, a stanje prethodnog retka $x$; dobivamo sljedeću jednadžbu prijelaza stanja: $f(i,j,l) = \sum f(i-1,x,l-sta(j))$.

Neka je redni broj stanja prethodnog retka $x$. Uz uvjet da trenutni i prethodni redak nisu u sukobu, prolazimo sva moguća $x$ i izvodimo prijelaz; jednadžba prijelaza je:

$$
f(i,j,l) = \sum f(i-1,x,l-sta(j))
$$

### Implementacija

??? note "Primjer rješenja"
    ```cpp
    --8<-- "docs/dp/code/state/state_1.cpp"
    ```

## Primjer 2

???+ note "[\[POI2004\] PRZ](https://www.luogu.com.cn/problem/P5911)"
    $n$ ljudi treba prijeći most; $i$-ta osoba ima težinu $w_i$ i prelazi most za vrijeme $t_i$. Ljudi se pri prelasku dijele u nekoliko skupina; tek kad svi iz jedne skupine prijeđu, ostale skupine mogu prelaziti. Najveća nosivost mosta je $W$. Koliko je najmanje vrijeme potrebno da svi prijeđu most?
    
    $100\le W \le 400$, $1\le n\le 16$, $1\le t_i\le 50$, $10\le w_i\le 100$.

### Objašnjenje

Neka $S$ označava podskup skupa svih ljudi, $t(S)$ najdulje vrijeme prelaska među ljudima u $S$, $w(S)$ ukupnu težinu ljudi u $S$, a $f(S)$ najmanje vrijeme potrebno da svi ljudi iz $S$ prijeđu most. Tada:

$$
\begin{cases}
    f(\varnothing)=0,\\
    f(S)=\min\limits_{T\subseteq S;~w(T)\leq W}\left\{t(T)+f(S\setminus T)\right\}.
\end{cases}
$$

Treba paziti da se ovdje ne mogu izravno prolaziti svi skupovi pa provjeravati jesu li podskupovi, nego treba koristiti [prolazak po podskupovima](../math/binary-set.md#遍历所有掩码的子掩码), čime vremenska složenost postaje $O(3^n)$.

### Implementacija

??? note "Primjer rješenja"
    ```cpp
    --8<-- "docs/dp/code/state/state_2.cpp"
    ```

## Zadaci za vježbu

-   [„NOI2001” Topnički položaji](https://loj.ac/problem/10173)
-   [„USACO06NOV” Corn Fields](https://www.luogu.com.cn/problem/P1879)
-   [„Zajednički ispit devet pokrajina 2018” Par drvenih figura](https://loj.ac/problem/2471)
