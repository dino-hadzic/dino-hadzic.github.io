---
title: Pickov teorem
---

## Pickov teorem

Pickov teorem: za jednostavan poligon čiji su svi vrhovi cjelobrojne točke, Pickov teorem daje vezu između njegove površine ${\displaystyle A}$, broja cjelobrojnih točaka u unutrašnjosti ${\displaystyle i}$ i broja cjelobrojnih točaka na rubu ${\displaystyle b}$: ${\displaystyle A=i+{\frac {b}{2}}-1}$.

Dokaz: [Pick's theorem](https://en.wikipedia.org/wiki/Pick%27s_theorem)

Teorem ima sljedeća poopćenja:

-   Uzmemo li površinu osnovnog lika rešetke za jedinicu, Pickov teorem vrijedi i na rešetki paralelograma. Na rešetki od proizvoljnih trokuta Pickov teorem glasi ${\displaystyle A=2 \times i+b-2}$.
-   Za poligon ${\displaystyle P}$ koji nije jednostavan, Pickov teorem glasi ${\displaystyle A=i+{\frac {b}{2}}-\chi (P)}$, gdje ${\displaystyle \chi (P)}$ označava **Eulerovu karakteristiku** poligona ${\displaystyle P}$.
-   Poopćenje na više dimenzije: Ehrhartovi polinomi.
-   Pickov teorem ekvivalentan je **Eulerovoj formuli** (${\displaystyle V-E+F=2}$).

## Primjer zadatka ([POJ 1265](http://poj.org/problem?id=1265))

### Sažetak zadatka

U pravokutnom koordinatnom sustavu robot kreće iz proizvoljne točke i napravi $\textit{n}$ pomaka; u svakom se pomakne za $\textit{dx}$ udesno i $\textit{dy}$ prema gore, pa na kraju nastaje zatvoren jednostavan poligon u ravnini. Odredite broj cjelobrojnih točaka na rubu, broj cjelobrojnih točaka unutar poligona i površinu poligona.

### Rješenje

Zadatak zapravo koristi sljedeće tri činjenice:

-   Dužina s cjelobrojnim krajevima, ako $\textit{dx}$ i $\textit{dy}$ nisu $0$, prolazi kroz $\gcd(\textit{dx}, \textit{dy}) + 1$ cjelobrojnih točaka; naravno, ako računamo za cijeli lik, dodatna točka već je uračunata u prethodnoj stranici, pa je ne treba dodavati. Dakle, broj točaka koje pokriva jedna stranica je $\gcd(\textit{dx},\textit{dy})$, gdje su $\textit{dx},\textit{dy}$ brojevi točaka koje dužina zauzima vodoravno odnosno okomito. Ako je $\textit{dx}$ ili $\textit{dy}$ jednak $0$, broj pokrivenih točaka je $\textit{dy}$ **odnosno** $\textit{dx}$.
-   Pickov teorem: površina jednostavnog poligona s cjelobrojnim vrhovima u ravnini = broj točaka na rubu/2 + broj točaka u unutrašnjosti - 1.
-   Površina proizvoljnog poligona jednaka je polovini zbroja vektorskih produkata vektora koje redom tvore susjedni vrhovi s ishodištem (to se može dobiti i određenim integralom u smjeru kazaljke na satu).

??? note "Referentni kôd"
    ```cpp
    --8<-- "docs/geometry/code/pick/pick_1.cpp"
    ```
