---
title: Bitovne operacije
---

Bitovne operacije su unarne i binarne operacije nad binarnim zapisom cijelih brojeva, a dijele se na **logičke operacije po bitovima** i **pomake**. Bitovne operacije pripadaju najosnovnijim operacijama procesora i obično su vrlo brze.

## Cijeli brojevi i nizovi bitova

Vidi i: [Cjelobrojni tipovi](../lang/var.md#整数类型), [Komplementi](./numeral-sys/base.md#补数法)

Niz fiksne duljine sastavljen samo od znakova `0` i `1` nazivamo nizom bitova. Krajnji lijevi bit nazivamo najvišim (najznačajnijim) bitom, a krajnji desni najnižim (najmanje značajnim) bitom.

Računala nizovima bitova prikazuju cijele brojeve iz određenog raspona. Nizova bitova duljine $N$ ima samo $2^N$, pa se mogu bijektivno pridružiti samo $2^N$ cijelih brojeva. Takva pridruživanja dijele se na dvije vrste: **s predznakom** (signed) i **bez predznaka** (unsigned). Pridruživanje s predznakom znači da među pridruženim cijelim brojevima ima negativnih, a bez predznaka da su svi pridruženi cijeli brojevi nenegativni.

-   Kod pridruživanja bez predznaka binarni zapis cijelog broja možemo izravno uzeti kao niz bitova; ako je zapis prekratak, dopunjujemo ga nulama `0` na višim mjestima.

    Uz pridruživanje bez predznaka niz bitova duljine $N$ može prikazati cijele brojeve iz $[0,2^N-1]$.

-   Kod pridruživanja s predznakom imamo dva pravila prikaza: **jedinični komplement** (ones' complement) i **dvojni komplement** (two's complement).

    Za nenegativne cijele brojeve pravilo prikaza isto je kao i bez predznaka. Za negativan cijeli broj uzmemo niz bitova njegova suprotnog broja i **invertiramo ga po bitovima** (tj. svaku `0` zamijenimo s `1`, a svaku `1` s `0`); rezultat nazivamo jediničnim komplementom. Ako jedinični komplement pretvorimo u cijeli broj prema pravilu bez predznaka, dodamo jedan, zatim ga prema pravilu bez predznaka pretvorimo natrag u niz bitova i odbacimo dio koji premašuje izvornu duljinu niza, dobiveni novi niz nazivamo dvojnim komplementom.

    Uz jedinični komplement niz bitova duljine $N$ može prikazati cijele brojeve iz $[-2^{N-1}+1,2^{N-1}-1]$.

    Uz dvojni komplement niz bitova duljine $N$ može prikazati cijele brojeve iz $[-2^{N-1},2^{N-1}-1]$.

Za primjer uzmimo nizove od $3$ bita:

| Niz bitova | Bez predznaka | S predznakom (jedinični komplement) | S predznakom (dvojni komplement) |
| ----- | ----- | --------- | --------- |
| `000` | $0$   | $0$       | $0$       |
| `001` | $1$   | $1$       | $1$       |
| `010` | $2$   | $2$       | $2$       |
| `011` | $3$   | $3$       | $3$       |
| `100` | $4$   | $-3$      | $-4$      |
| `101` | $5$   | $-2$      | $-3$      |
| `110` | $6$   | $-1$      | $-2$      |
| `111` | $7$   | $-0$      | $-1$      |

Vidimo da je najveći problem jediničnog komplementa pojava „negativnog broja” $-0$, koji zapravo ne postoji, pa u pravilu koristimo samo dvojni komplement. Budući da pri prikazu cijelih brojeva s predznakom o predznaku odlučuje isključivo najviši bit niza, taj bit nazivamo **bitom predznaka**.

Pretvaranje niza bitova u cijeli broj također je jednostavno: za nenegativne brojeve nije potrebno ništa posebno, kod jediničnog komplementa inverzijom dobivamo suprotni broj, a kod dvojnog komplementa suprotni broj dobivamo inverzijom i dodavanjem jedinice.

## Logičke operacije po bitovima

Logičke operacije po bitovima su operacije koje na niz bitova, bit po bit, primjenjuju neke [Booleove funkcije](./boolean-algebra.md#布尔函数). Formalno, za Booleovu funkciju $f:\mathbf{B}^k\to \mathbf{B}$ operacija po bitovima jest funkcija oblika

$$
\begin{aligned}
    F:\left(\mathbf{B}^m\right)^k&\to \mathbf{B}^m\\
    ((p_{1,1},\dots,p_{m,1}),\dots,(p_{1,k},\dots,p_{m,k}))&\mapsto (f(p_{1,1},\dots,p_{1,k}),\dots,f(p_{m,1},\dots,p_{m,k}))
\end{aligned}
$$

gdje je $m$ duljina niza bitova. Kao i inače, u pravilu proučavamo samo unarne i binarne operacije po bitovima. Ako nije drukčije rečeno, operacije po bitovima u nastavku ograničene su na unarni i binarni slučaj.

Općenito, **negaciju po bitovima (NOT)**, **I po bitovima (AND)**, **ILI po bitovima (OR)** i **isključivo ILI po bitovima (XOR)** smatramo osnovnim operacijama po bitovima; sve ostale operacije po bitovima mogu se dobiti njihovim kombiniranjem.

| Operacija po bitovima | Matematička oznaka | Pripadna Booleova funkcija | Operator u C++-u | Objašnjenje |
| ---- | ----------------------------- | -------- | --------------- | ----------------------- |
| negacija po bitovima (NOT) | $\operatorname{NOT}$          | $\lnot$  | `~`             | $0$ postaje $1$, a $1$ postaje $0$   |
| I po bitovima (AND)  | $\operatorname{AND}$          | $\land$  | `&`             | rezultat je $1$ samo ako su oba odgovarajuća bita $1$   |
| ILI po bitovima (OR)  | $\operatorname{OR}$           | $\lor$   | <code>\|</code> | rezultat je $1$ čim je barem jedan od dvaju odgovarajućih bitova $1$ |
| isključivo ILI po bitovima (XOR) | $\oplus$, $\operatorname{XOR}$ | $\oplus$ | `^`             | rezultat je $1$ samo ako su dva odgovarajuća bita različita        |

???+ warning "Upozorenje"
    Pazite na razliku između operacija po bitovima i Booleovih funkcija.

Na primjer:

-   $\operatorname{NOT} 01010111=10101000$,
-   $01010011 \operatorname{AND} 00110010=00010010$,
-   $01010011 \operatorname{OR}  00110010=01110011$,
-   $01010011 \operatorname{XOR} 00110010=01100001$.

Budući da se pri izvođenju gornjih četiriju operacija po bitovima računanje na pojedinim bitovima odvija neovisno, te četiri operacije izravno nasljeđuju svojstva pripadnih Booleovih funkcija.

Radi jednostavnosti, kad je duljina niza bitova poznata, operacije po bitovima možemo primjenjivati izravno na cijele brojeve, npr.:

$$
\begin{aligned}
    \operatorname{NOT} 5&=-6,\\
    \operatorname{NOT} (-5)&=4,\\
    5 \operatorname{AND} 6 &=4,\\
    5 \operatorname{OR} 6 &=7,\\
    5 \operatorname{XOR} 6 &=3.
\end{aligned}
$$

Uz pretpostavku $x,y\geq 0$ operacije po bitovima možemo zapisati i pomoću suma:

$$
\begin{aligned}
    \operatorname{NOT} x&=\sum_{n=0}^{\lfloor\log_{2}x\rfloor}2^n\left(\left(\left\lfloor\frac{x}{2^n}\right\rfloor\bmod 2+1\right)\bmod 2\right)\\
    &=\sum_{n=0}^{\lfloor\log_{2}x\rfloor}\left(2^{\left\lfloor\log_{2}x\right\rfloor +1}-1-x\right)\\
    x\operatorname{AND} y&=\sum_{n=0}^{\lfloor\log_{2}\max\{x,y\}\rfloor}2^n\left(\left\lfloor\frac{x}{2^n}\right\rfloor\bmod 2\right)\left(\left\lfloor{\frac{y}{2^n}}\right\rfloor\bmod 2\right)\\
    x\operatorname{OR} y&=\sum_{n=0}^{\lfloor\log_{2}\max\{x,y\}\rfloor}2^n\left(\left(\left\lfloor\frac{x}{2^n}\right\rfloor\bmod 2\right)+\left(\left\lfloor{\frac{y}{2^n}}\right\rfloor\bmod 2\right)-\left(\left\lfloor\frac{x}{2^n}\right\rfloor\bmod 2\right)\left(\left\lfloor{\frac{y}{2^n}}\right\rfloor\bmod 2\right)\right)\\
    x\operatorname{XOR} y&=\sum_{n=0}^{\lfloor\log_{2}\max\{x,y\}\rfloor}2^n\left(\left(\left(\left\lfloor\frac{x}{2^n}\right\rfloor\bmod 2\right)+\left(\left\lfloor{\frac{y}{2^n}}\right\rfloor\bmod 2\right)\right)\bmod 2\right)\\
    &=\sum_{n=0}^{\lfloor\log_{2}\max\{x,y\}\rfloor}2^n\left(\left(\left\lfloor\frac{x}{2^n}\right\rfloor +\left\lfloor\frac{y}{2^n}\right\rfloor\right)\bmod 2\right)
\end{aligned}
$$

Kad ne postoji opasnost od zabune, u nastavku izostavljamo „po bitovima”.

## Pomak bitova

Vidi i: [Bitovni operatori u C++-u](../lang/op.md#位操作符).

Pomak (shift) je binarna operacija koja niz bitova „pomiče ulijevo ili udesno bit po bit”; prvi je argument niz bitova, a drugi je u pravilu nenegativan cijeli broj. Pomicanje ulijevo zovemo **lijevim pomakom**, a udesno **desnim pomakom**. Prema načinu popunjavanja mjesta ispražnjenih pomicanjem pomake dijelimo na **aritmetičke**, **logičke** i **kružne (rotacije)**. Pri tome

-   logički pomak ispražnjena mjesta popunjava nulama 0,
-   aritmetički desni pomak ispražnjena mjesta popunjava bitom predznaka, a aritmetički lijevi pomak jednak je logičkom lijevom pomaku,
-   kružni pomak ispražnjena mjesta popunjava bitovima koji su ispali.

Na primjer, za $8$-bitni niz `10 01 01 10`:

| Operacija         | Rezultat            |
| ---------- | ------------- |
| aritmetički pomak ulijevo za $2$ bita | `01 01 10 00` |
| aritmetički pomak udesno za $2$ bita | `11 10 01 01` |
| logički pomak ulijevo za $2$ bita | `01 01 10 00` |
| logički pomak udesno za $2$ bita | `00 10 01 01` |
| kružni pomak ulijevo za $2$ bita | `01 01 10 10` |
| kružni pomak udesno za $2$ bita | `10 10 01 01` |

U C++-u lijevi pomak zapisujemo kao `a << b`, a desni kao `a >> b`; koje se pravilo pomaka pri tome primjenjuje, vidi [Bitovni operatori u C++-u](../lang/op.md#位操作符).

Kružni pomak možemo implementirati sljedećim kodom:

???+ note "Implementacija"
    ```cpp
    --8<-- "docs/math/code/bit/bit_1.cpp:core"
    ```

## Primjene bitovnih operacija

Bitovne operacije u pravilu imaju tri uloge:

1.  Učinkovito izvođenje nekih računskih operacija umjesto drugih, sporijih načina. Vidi [Optimizacije pri prevođenju – smanjenje snage operacija](../lang/optimizations.md#强度削减-strength-reduction).
2.  [Prikaz skupova](./binary-set.md) (često u [DP-u s bitmaskama](../dp/state.md)).
3.  Zadatak sam po sebi zahtijeva bitovne operacije.

Treba imati na umu da zamjena drugih operacija bitovnima često ne donosi veliko ubrzanje, a kod čini složenijim, pa to pri uporabi treba dobro odvagnuti.

### Primjene vezane uz potencije broja 2

Budući da bitovne operacije rade nad binarnim zapisom, iz njih proizlaze mnoge primjene vezane uz cjelobrojne potencije broja 2.

Množenje (dijeljenje) broja nenegativnom cjelobrojnom potencijom broja 2:

=== "C++"
    ```cpp
    --8<-- "docs/math/code/bit/bit_2.cpp:mul"
    ```

=== "Python"
    ```python
    --8<-- "docs/math/code/bit/bit_2.py:mul"
    ```

??? warning "Upozorenje"
    Dijeljenje kakvo obično pišemo zaokružuje prema $0$, a desni pomak ovdje zaokružuje prema dolje (pazite na tu razliku); dakle, za brojeve veće ili jednake $0$ oba su načina ekvivalentna, a za brojeve manje od $0$ postoji razlika, npr. vrijednost `-1 / 2` jest $0$, a vrijednost `-1 >> 1` jest $-1$.

### Apsolutna vrijednost

Na nekim je strojevima učinkovitije od `n > 0 ? n : -n`.

=== "C++"
    ```cpp
    --8<-- "docs/math/code/bit/bit_2.cpp:abs"
    ```

=== "Python"
    ```python
    --8<-- "docs/math/code/bit/bit_2.py:abs"
    ```

### Maksimum/minimum dvaju brojeva

Na nekim je strojevima učinkovitije od `a > b ? a : b`.

=== "C++"
    ```cpp
    --8<-- "docs/math/code/bit/bit_2.cpp:minmax"
    ```

=== "Python"
    ```python
    --8<-- "docs/math/code/bit/bit_2.py:minmax"
    ```

### Provjera imaju li dva broja različita od nule isti predznak

=== "C++"
    ```cpp
    --8<-- "docs/math/code/bit/bit_2.cpp:sgn"
    ```

=== "Python"
    ```python
    --8<-- "docs/math/code/bit/bit_2.py:sgn"
    ```

### Zamjena dvaju brojeva

???+ note "Metoda ima ograničenja"
    Ovim se načinom mogu zamijeniti samo dva cijela broja, pa je raspon primjene ograničen.
    
    Za zamjenu u općem slučaju preporučuje se izravno pozvati funkciju `std::swap` iz biblioteke `algorithm`.

```cpp
--8<-- "docs/math/code/bit/bit_2.cpp:swap"
```

### Rad s pojedinim bitovima broja

Dohvaćanje određenog bita binarnog zapisa broja:

=== "C++"
    ```cpp
    --8<-- "docs/math/code/bit/bit_2.cpp:get_bit"
    ```

=== "Python"
    ```python
    --8<-- "docs/math/code/bit/bit_2.py:get_bit"
    ```

Postavljanje određenog bita binarnog zapisa broja na $0$:

=== "C++"
    ```cpp
    --8<-- "docs/math/code/bit/bit_2.cpp:unset_bit"
    ```

=== "Python"
    ```python
    --8<-- "docs/math/code/bit/bit_2.py:unset_bit"
    ```

Postavljanje određenog bita binarnog zapisa broja na $1$:

=== "C++"
    ```cpp
    --8<-- "docs/math/code/bit/bit_2.cpp:set_bit"
    ```

=== "Python"
    ```python
    --8<-- "docs/math/code/bit/bit_2.py:set_bit"
    ```

Invertiranje određenog bita binarnog zapisa broja:

=== "C++"
    ```cpp
    --8<-- "docs/math/code/bit/bit_2.cpp:flap_bit"
    ```

=== "Python"
    ```python
    --8<-- "docs/math/code/bit/bit_2.py:flap_bit"
    ```

Ove operacije zapravo tretiraju $32$-bitnu cjelobrojnu varijablu kao Booleovo polje duljine $32$.

## Hammingova težina

Hammingova težina niza simbola jest broj simbola različitih od nul-simbola (zero-symbol, definiranog nad korištenom abecedom). Za binarni broj Hammingova težina jednaka je broju njegovih jedinica $1$ (tj. `popcount`).

Hammingovu težinu broja možemo izračunati petljom: neprestano uklanjamo posljednji bit binarnog zapisa broja (tj. pomičemo ga udesno za $1$ bit), održavamo varijablu s odgovorom i tijekom dijeljenja ažuriramo odgovor ovisno o tome je li najniži bit $1$.

Kod je sljedeći:

```cpp
--8<-- "docs/math/code/bit/bit_2.cpp:popcnt1"
```

Hammingovu težinu broja možemo izračunati i operacijom `lowbit`: od broja neprestano oduzimamo njegov `lowbit`[^note1] dok broj ne postane $0$.

Kod je sljedeći:

```cpp
--8<-- "docs/math/code/bit/bit_2.cpp:popcnt2"
```

### Konstrukcija permutacije s rastućom Hammingovom težinom

U [DP-u s bitmaskama](../dp/state.md) nabrajanje stanja u poretku rastućeg popcounta ponekad omogućuje izbjegavanje ponovnog nabrajanja istih stanja. To je jedna od glavnih primjena konstrukcije permutacije s rastućom Hammingovom težinom.

U nastavku konkretno istražujemo kako u vremenu $O(n)$ konstruirati permutaciju s rastućom Hammingovom težinom.

Znamo da je najmanji cijeli broj Hammingove težine $n$ jednak $2^n-1$. Ako za cijeli broj u konstantnom vremenu možemo konstruirati sljedbenika jednake Hammingove težine, onda nabrajanjem Hammingovih težina i neprestanim traženjem sljedećeg broja počevši od $2^n-1$ u vremenu $O(n)$ konstruiramo traženu permutaciju brojeva $0\sim n$.

Sljedbenika broja $x$ s jednakom Hammingovom težinom pronalazimo prema ovoj ideji, na primjeru $(10110)_2$:

-   Krajnju desnu jedinicu $1$ broja $(10110)_2$ pomaknemo ulijevo; ako se ne može pomaknuti, pomaknemo jedinicu $1$ lijevo od nje, i tako dalje. Dobivamo $(11010)_2$.

-   U dobivenom $(11010)_2$ sve jedinice $1$ od izvornog položaja posljednje pomaknute jedinice $1$ do najnižeg bita pomaknemo skroz udesno. Ovdje je posljednja pomaknuta jedinica $1$ izvorno bila na trećem mjestu, pa posljednja tri bita $010$ moraju postati $001$ i dobivamo $(11001)_2$.

Taj se postupak može optimizirati bitovnim operacijama:

```cpp
--8<-- "docs/math/code/bit/bit_3.cpp:hamming1"
```

-   U prvom koraku broju $x$ dodajemo njegov `lowbit`, što u binarnom zapisu znači da krajnji desni neprekinuti blok jedinica $1$ broja $x$ zamjenjujemo jednom jedinicom $1$ lijevo od njega. Primjerice, maloprije spomenuti binarni broj $(10110)_2$ nakon dodavanja svojeg `lowbit`-a postaje $(11000)_2$. Time smo zapravo dobili prvu polovicu odgovora.
-   Zatim moramo nadopuniti jedinice $1$ na kraju odgovora. `lowbit` od $t$ jest položaj na koji je pomaknuta krajnja lijeva jedinica $1$ krajnjeg desnog neprekinutog bloka jedinica $1$ broja $x$, a `lowbit` od $x$ jest položaj krajnje desne jedinice $1$ tog bloka broja $x$. Opet na primjeru $(10110)_2$: $t = (11000)_2$, $\operatorname{lowbit}(t) = (01000)_2$, $\operatorname{lowbit}(x)=(00010)_2$.
-   Dijeljenje koje slijedi najteži je dio ove bitovne tehnike za razumijevanje, ali i najvažniji. Neka se najviša jedinica $1$ krajnjeg desnog neprekinutog bloka jedinica $1$ **izvornog broja** nalazi na $r$-tom bitu (bitove brojimo od $0$), a najniža jedinica $1$ na $l$-tom bitu; `lowbit` od $t$ jednak je `1 << (r+1)`, `lowbit` od $x$ jednak je `1 << l`, a `(((t&-t)/(x&-x))>>1)` daje `(1<<(r+1))/(1<<l)/2 = (1<<r)/(1<<l) = 1<<(r-l)`, što je u binarnom zapisu jedinica $1$ iza koje slijedi $r-l$ nula, a broj nula upravo je jednak broju uzastopnih jedinica $1$ umanjenom za $1$. Na našem primjeru: $\frac{\operatorname{lowbit(t)/2}}{\operatorname{lowbit(x)}} = \frac{(00100)_2}{(00010)_2} = (00010)_2$. Oduzmemo li od tog broja $1$, dobivamo upravo niže bitove koje treba nadopuniti, a OR s izvornim brojem daje odgovor.

Potpuni kod za nabrajanje permutacije brojeva $0\sim n$ u poretku rastuće Hammingove težine stoga glasi:

```cpp
--8<-- "docs/math/code/bit/bit_3.cpp:hamming2_begin"
--8<-- "docs/math/code/bit/bit_3.cpp:hamming2_end"
```

Pri tome treba posebno obraditi $0$, jer $0$ nema sljedbenika iste Hammingove težine.

## Srodne klase i funkcije u C++-u

### Ugrađene funkcije GCC-a

GCC ima i nekoliko ugrađenih (built-in) funkcija za bitovne operacije:

-   `int __builtin_ffs(int x)`: vraća položaj posljednje jedinice $1$ na kraju binarnog zapisa od $x$; položaji se broje od $1$ (najniži bit ima broj $1$). Kad je $x$ jednak $0$, vraća $0$.
-   `int __builtin_clz(unsigned int x)`: vraća broj vodećih nula $0$ u binarnom zapisu od $x$. Kad je $x$ jednak $0$, rezultat nije definiran.
-   `int __builtin_ctz(unsigned int x)`: vraća broj uzastopnih nula $0$ na kraju binarnog zapisa od $x$. Kad je $x$ jednak $0$, rezultat nije definiran.
-   `int __builtin_clrsb(int x)`: kad je bit predznaka od $x$ jednak $0$, vraća broj vodećih nula $0$ u binarnom zapisu od $x$ umanjen za jedan; inače vraća broj vodećih jedinica $1$ u binarnom zapisu od $x$ umanjen za jedan.
-   `int __builtin_popcount(unsigned int x)`: vraća broj jedinica $1$ u binarnom zapisu od $x$.
-   `int __builtin_parity(unsigned int x)`: određuje parnost broja jedinica $1$ u binarnom zapisu od $x$.

Svim ovim funkcijama na kraj imena možemo dodati `l` ili `ll` (npr. `__builtin_popcountll`) kako bi tip argumenta postao (`unsigned`)`long` odnosno (`unsigned`)`long long` (povratna vrijednost i dalje je tipa `int`).
Primjerice, ponekad želimo izračunati logaritam broja po bazi dva; ako zanemarimo poseban slučaj `0`, to je jednako broju bitova binarnog zapisa tog broja `-1`, a broj bitova binarnog zapisa `N`-bitnog cijelog broja `n` može se izraziti kao `N - __builtin_clz(n)`, pa `N - 1 - __builtin_clz(n)` daje logaritam od `n` po bazi dva.

Budući da su to ugrađene funkcije koje prevodilac snažno optimizira, izvršavaju se vrlo brzo (nekima je dovoljna čak samo jedna instrukcija).

### Više bitova

Ako je niz bitova s kojim treba raditi vrlo dug, može se koristiti [`std::bitset`](../lang/csl/bitset.md).

## Preporučeni zadaci

-   [Luogu P1225 黑白棋游戏 (Igra s crno-bijelim figurama)](https://www.luogu.com.cn/problem/P1225)

## Literatura i napomene

1.  [Trikovi s bitovnim operacijama](https://graphics.stanford.edu/~seander/bithacks.html)
2.  [Bit Operation Builtins (Using the GNU Compiler Collection (GCC))](https://gcc.gnu.org/onlinedocs/gcc/Bit-Operation-Builtins.html)
3.  [Bitwise operation - Wikipedia](https://en.wikipedia.org/wiki/Bitwise_operation)

[^note1]: Prva jedinica $1$ binarnog zapisa broja gledano od nižih bitova prema višima, zajedno s nulama iza nje; npr. `lowbit` od $(1010)_2$ jest $(0010)_2$. Pojedinosti vidi u [Fenwickovo stablo](../ds/fenwick.md).
