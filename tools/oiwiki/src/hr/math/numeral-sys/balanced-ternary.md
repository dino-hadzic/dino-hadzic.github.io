---
title: Balansirani ternarni sustav
---

## Definicija

Balansirani ternarni sustav (balanced ternary) naziva se i simetrični ternarni sustav. Riječ je o poopćenom pozicijskom brojevnom sustavu.

Znamenke običnog ternarnog sustava čine `0`, `1` i `2`, dok znamenke balansiranog ternarnog sustava čine `-1`, `0` i `1`. Njegova je baza također `3` (jer postoje tri moguće vrijednosti). Budući da je nezgodno pisati `-1` kao znamenku, umjesto `-1` koristit ćemo slovo `Z`.

## Objašnjenje

Evo nekoliko primjera:

| dekadski | balansirani ternarni | dekadski | balansirani ternarni |
| --- | ----- | --- | ----- |
| `0` | `0`   | `5` | `1ZZ` |
| `1` | `1`   | `6` | `1Z0` |
| `2` | `1Z`  | `7` | `1Z1` |
| `3` | `10`  | `8` | `10Z` |
| `4` | `11`  | `9` | `100` |

Negativni brojevi u ovom se brojevnom sustavu prikazuju vrlo jednostavno: dovoljno je zamijeniti znamenke pozitivnog broja (`Z` postaje `1`, `1` postaje `Z`).

| dekadski | balansirani ternarni |
| ---- | ----- |
| `-1` | `Z`   |
| `-2` | `Z1`  |
| `-3` | `Z0`  |
| `-4` | `ZZ`  |
| `-5` | `Z11` |

Lako je uočiti da je najviša znamenka negativnog broja `Z`, a pozitivnog `1`.

## Postupak

Kod pretvorbe u balansirani ternarni sustav najprije treba zapisati zadani broj `x` u standardnom ternarnom sustavu. Kad je `x` zapisan u standardnom ternarnom sustavu, svaka je njegova znamenka `0`, `1` ili `2`. Iteriramo počevši od najniže znamenke: znamenke `0` i `1` možemo preskočiti, ali ako naiđemo na `2`, trebamo je pretvoriti u `Z` i sljedećoj znamenki dodati `1`. Ako naiđemo na znamenku `3`, trebamo je pretvoriti u `0` i sljedećoj znamenki dodati `1`.

### Primjer 1

Pretvorimo `64` u balansirani ternarni sustav.

Najprije zapišimo taj broj u standardnom ternarnom sustavu:

$$
\text 64_{10} = 02101_3
$$

Krenimo od znamenke koja najmanje utječe na cijeli broj (najniže znamenke):

-   `101` se preskače (jer su `0` i `1` dopušteni u balansiranom ternarnom sustavu);
-   `2` postaje `Z`, a znamenki lijevo od nje dodaje se `1`; dobivamo `1Z101`;
-   `1` se preskače; dobivamo `1Z101`.

Konačni je rezultat `1Z101`.

Pretvorimo ga natrag u dekadski sustav:

$$
\texttt {1Z101}=81 \times 1 +27 \times (-1) + 9 \times 1 + 3 \times 0 + 1 \times 1 = 64_{10}
$$

### Primjer 2

Pretvorimo `237` u balansirani ternarni sustav.

Najprije zapišimo taj broj u standardnom ternarnom sustavu:

$$
\text 237_{10} = 22210_3
$$

-   `0` i `1` se preskaču (jer su `0` i `1` dopušteni u balansiranom ternarnom sustavu);
-   `2` postaje `Z`, a znamenki lijevo dodaje se `1`; dobivamo `23Z10`;
-   `3` postaje `0`, a znamenki lijevo dodaje se `1`; dobivamo `30Z10`;
-   `3` postaje `0`, a znamenki lijevo (podrazumijevano `0`) dodaje se `1`; dobivamo `100Z10`;
-   `1` se preskače; dobivamo `100Z10`.

Konačni je rezultat `100Z10`.

Pretvorimo ga natrag u dekadski sustav:

$$
\texttt{100Z10} = 243 \cdot 1 + 81 \cdot 0 + 27 \cdot 0 + 9 \cdot (-1) + 3 \cdot 1 + 1 \cdot 0 = 237_{10}
$$

## Svojstva

Za balansirani ternarni broj $X_3$ možemo svaku znamenku $x_i$ pomnožiti odgovarajućom težinom $3^i$ i tako jednoznačno dobiti dekadski broj $Y_{10}$.

Odgovara li onda dekadskom broju $Y_{10}$ **jednoznačno jedan balansirani ternarni broj**?

Odgovor je potvrdan; to se svojstvo naziva jedinstvenost balansiranog ternarnog sustava.

???+ note "Dokaz"
    Dokazujemo **svođenjem na kontradikciju**:
    
    Pretpostavimo da za dekadski broj $Y_{10}$ postoje dva **različita balansirana ternarna broja** $A_3,B_3$ koja pretvorena u dekadski sustav daju $Y_{10}$; treba dokazati $A_3 = B_3$. Razlikujemo slučajeve:
    
    1.  Kad je $Y_{10}=0$, očito je $A_3 = B_3 = 0_3$, što je u suprotnosti s pretpostavkom.
    2.  Kad je $Y_{10}>0$:
    
        -   Numerirajmo znamenke brojeva $A_3$ i $B_3$ od najniže prema najvišoj; neka je $a_i$ $i$-ta znamenka od $A_3$, a $b_i$ $i$-ta znamenka od $B$. U $A_3,B_3$ nužno postoji $i$ takav da je $a_i\neq b_i$. Uočimo da znamenke $i-1,i-2,\dots,0$ nisu bitne za dokaz. Stoga $A_3,B_3$ pomaknemo udesno za $i$ znamenaka i dobijemo $A_3',B_3'$; izvorni je problem ekvivalentan dokazivanju $A_3'=B_3'$.
        -   Za $0$-tu znamenku brojeva $A_3',B_3'$ vrijedi $a_0 \neq b_0$. Pretpostavimo $b_0 > a_0$ (za $a_0>b_0$ rezultat je isti); lako se vidi $b_0 - a_0 \in \{1,2\}$. Doprinos znamenaka $i=1,2,3,\dots$ broja $A_3'$ vrijednosti od $A_3'$ iznosi $S_1 = a_1 \times 3^1 + a_2 \times 3^2+ \dots$, a doprinos znamenaka $i=1,2,3,\dots$ broja $B_3'$ vrijednosti od $B_3'$ iznosi $S_2 = b_1 \times 3^1 + b_2 \times 3^2 + \dots$. Budući da je $A_3' = B_3'$, dobivamo $S_1 - S_2 = b_0 - a_0$. $S_1,S_2$ imaju zajednički faktor $3$, a $b_0 - a_0$ nije djeljiv s $3$, što je u suprotnosti s pretpostavkom; stoga je $A_3'\neq B_3'$
    3.  Kad je $Y_{10}<0$, dokaz je isti kao za $Y_{10}>0$.
    
    Dakle, svakom dekadskom broju $Y_{10}$ odgovara jedinstveni balansirani ternarni broj $X_3$.

## Zadaci za vježbu

[Topcoder SRM 604 PowerOfThree](https://archive.topcoder.com/ProblemStatement/pm/12917)

**Ova je stranica dijelom prevedena iz članka [Троичная сбалансированная система счисления](http://e-maxx.ru/algo/balanced_ternary) i njegova engleskog prijevoda [Balanced Ternary](https://cp-algorithms.com/algebra/balanced-ternary.html). Ruska je inačica objavljena pod licencijom Public Domain + Leave a Link, a engleska pod CC-BY-SA 4.0.**
