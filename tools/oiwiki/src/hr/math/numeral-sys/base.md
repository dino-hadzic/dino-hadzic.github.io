---
title: Baza brojevnog sustava
---

**Pozicijski brojevni sustav** (positional numeral system), koji se naziva i **sustav s prijenosom** (carry system), **sustav baze**, **pozicijski zapis** (positional notation), **zapis mjesnih vrijednosti** (place-value notation), **pozicijski sustav brojevnih vrijednosti**, brojevni je sustav koji konačnim brojem simbola može prikazati sve prirodne brojeve. Broj simbola koje pozicijski sustav može koristiti naziva se **baza** (radix, base); pozicijski sustav s bazom $n$ naziva se sustav s bazom $n$ ($n>1$); na primjer, dekadski sustav koji najčešće koristimo za zapis brojeva obično koristi samo deset simbola `0, 1, 2, 3, 4, 5, 6, 7, 8, 9`. Prijenos je operacija „kad neka znamenka broja dosegne bazu, postavi je na 0 i znamenku na sljedećem višem mjestu uvećaj za jedan”.

Općenito, broj u sustavu s bazom $n$ zapisujemo kao $(a_k\cdots a_1a_0)_n$, $(a_k\cdots a_1a_0)_{(n)}$, ${a_k\cdots a_1a_0}_{(n)}$, ${a_k\cdots a_1a_0}_{n}$ i slično. Ako je baza jasna iz konteksta, indeks možemo izostaviti. Napomena: $a_k\cdots a_1a_0$ ovdje nije umnožak $k+1$ brojeva, nego niz.

Za broj $a_n\cdots a_1a_0$ u sustavu s bazom $k$ vrijednost koju predstavlja jest $a_nk^n+\cdots+a_1k^1+a_0k^0=\sum_{i=0}^n a_ik^i$; za broj $m$ čiji je zapis u bazi $k$ jednak $a_n\cdots a_1a_0$ vrijedi:

$$
\begin{array}{cc}
    a_0=m-q_0k,&q_0=f(m/k),\\
    a_1=q_0-q_1k,&q_1=f(q_0/k),\\
    \vdots&\vdots\\
    a_n=q_{n-1}-q_nk,&q_n=f(q_{n-1}/k)=0,\\
\end{array}
$$

gdje je $f(x)=\lfloor x\rfloor$.

Duljina zapisa broja $n$ u bazi $k$ iznosi $\lceil\log_k (n+1)\rceil$.

Obično decimalne brojeve prikazujemo dodavanjem decimalne točke „$.$”[^note4], negativne brojeve dodavanjem predznaka „$-$”, beskonačne periodične decimalne brojeve crtom iznad završnog dijela decimala itd. Radi lakšeg čitanja možemo svakih nekoliko znamenaka umetnuti razdjelnik (npr. razmak, $,$, `'` itd.); na primjer, $12~345$ označava $12345$.

U računalstvu su češći pozicijski sustavi binarni, oktalni i heksadekadski.

## Pretvorba između različitih baza

### Iz dekadskog u druge sustave

Postupak pokazujemo na primjeru binarnog sustava; za ostale baze načelo je slično.

Za cijeli dio dekadski broj uzastopno dijelimo s $2$ dok kvocijent ne postane $0$, a zatim odozdo prema gore uzmemo sve ostatke; to su znamenke cijelog dijela binarnog broja. Za razlomljeni dio množimo ga s $2$ i uzmemo cijeli dio rezultata, zatim isti postupak ponavljamo s dobivenim razlomljenim dijelom sve dok razlomljeni dio ne postane $0$; nakon toga odozgo prema dolje uzmemo cijele dijelove svih rezultata; to su znamenke razlomljenog dijela binarnog broja.

???+ example "Primjer"
    Pretvorimo $35.25$ u binarni broj.
    
    Cijeli dio:
    
    $$
    \begin{aligned}
        35/2&=17  &\dots 1,\\
        17/2&=8   &\dots 1,\\
        8/2&=4    &\dots 0,\\
        4/2&=2    &\dots 0,\\
        2/2&=1    &\dots 0,\\
        1/2&=0    &\dots 1.
    \end{aligned}
    $$
    
    Razlomljeni dio:
    
    $$
    \begin{aligned}
        0.25\times 2&=0.5  &\dots 0,\\
        0.5\times 2&=1     &\dots 1.
    \end{aligned}
    $$
    
    Dakle, $35.25 = (100011.01)_2$.

???+ note "Implementacija"
    ```cpp
    --8<-- "docs/math/code/base/base_1.cpp:from_dec"
    ```

### Iz drugih sustava u dekadski

Opet na primjeru binarnog sustava. Za pretvorbu binarnog broja u dekadski dovoljno je vrijednost svake znamenke pomnožiti s $2^i$, gdje je $i$ pozicija trenutačne znamenke, a znamenka jedinica ima poziciju $0$.

???+ example "Primjer"
    Pretvorimo $(11010.01)_{2}$ u dekadski broj.
    
    $$
    \begin{aligned}
        (11010.01)_{2}&=\phantom{+~}1\times 2^4+1\times 2^3+0\times 2^2+1\times 2^1+0\times 2^0\\
        &\phantom{=}+~0\times 2^{-1}+1\times 2^{-2} \\
                    &=26.25.
    \end{aligned}
    $$
    
    Dakle, $(11010.01)_2 = (26.25)_{10}$.

???+ note "Implementacija"
    ```cpp
    --8<-- "docs/math/code/base/base_1.cpp:to_dec"
    ```

### Međusobna pretvorba binarnog, oktalnog i heksadekadskog sustava

Jedna oktalna znamenka može se prikazati s 3 binarne znamenke (jer je $2^3 = 8$), a jedna heksadekadska znamenka s 4 binarne znamenke ($2^4 = 16$), i obrnuto.

## Metoda komplemenata

Vidi također: [Jedinični i dvojni komplement](../bit.md#整数与位序列)

**Metoda komplemenata** (method of complements) postupak je kojim se negativni brojevi prikazuju pozitivnima tako da se oduzimanje može izvesti istim algoritmom/sklopom/mehaničkom konstrukcijom kao zbrajanje pozitivnih brojeva. Metoda komplemenata široko se koristi u dizajnu kalkulatora i računala radi pojednostavljenja konstrukcije.

Za $n$-znamenkasti broj $a$ u bazi $b$ njegov je **komplement baze** (radix complement, tzv. $b$-komplement) $b^n-a$, a njegov **umanjeni komplement baze** (diminished radix complement, tzv. $b-1$-komplement, kraće **umanjeni komplement**) jest $b^n-1-a$. U binarnom sustavu komplement baze naziva se komplement broja $2$ (two's complement), tj. **dvojni komplement**; umanjeni komplement baze naziva se komplement broja $1$ (ones' complement), tj. **jedinični komplement**; u dekadskom sustavu komplement baze naziva se i komplement broja $10$ (ten's complement), a umanjeni komplement baze komplement broja $9$ (nine's complement); za ostale baze analogno.

Za $n$-znamenkaste brojeve $x,y$ u bazi $b$ pri računanju $x-y$ imamo sljedeće postupke (ako rezultat premašuje $n$ znamenaka, više znamenke odbacujemo):

1.  Uzmemo umanjeni komplement $x'=b^n-1-x$ broja $x$ i izračunamo $x'+y=b^n-1-x+y$; umanjeni komplement tog rezultata jest odgovor.
2.  Uzmemo umanjeni komplement $y'=b^n-1-y$ broja $y$ i izračunamo $x+y'=b^n-1+x-y$; dodavanjem jedinice odmah dobivamo odgovor.
3.  Uzmemo komplement baze $x'=b^n-x$ broja $x$ i izračunamo $x'+y=b^n-x+y$; komplement baze tog rezultata jest odgovor.
4.  Uzmemo komplement baze $y'=b^n-y$ broja $y$ i izračunamo $x+y'=b^n+x-y$; to je odgovor.

Osim toga, za brojeve u bazi $k$ stavimo $d=k-1$; tada je $\cdots dd=:\overline{d}=\sum_{i=0}^{\infty} dk^i=-1$, pa za $n$-znamenkasti broj $x$ čiji je komplement baze u bazi $k$ zapisan kao $a_{n-1}\cdots a_1a_0$ vrijedi da je $\overline{d}a_{n-1}\cdots a_1a_0$ jednako $\sum_{i=0}^{n-1}a_ik^i+\sum_{i=n}^{\infty} dk^i=k^n-x+(-k^n)=-x$. Ova ideja „brojeva s beskonačno mnogo znamenaka” poopćuje se u [**$p$-adske brojeve**](https://en.wikipedia.org/wiki/P-adic_number) ($p$-adic number).

Uz to, postoji zanimljiv teorem o komplementima i beskonačnim periodičnim decimalnim brojevima:

???+ note "Midyjev teorem"
    Neka je $a$ pozitivan cijeli broj, $p$ pozitivan prost broj, a zapis $a/p$ u bazi $b$ jednak $0.\overline{a_1a_2\cdots a_l}$, gdje je $l$ duljina (najkraćeg) perioda. Ako je $l$ paran[^note5], neka je $l=2k$; tada je $a_1a_2\cdots a_k$ umanjeni komplement od $a_{k+1}a_{k+2}\cdots a_{2k}$, tj.:
    
    -   $a_i+a_{i+k}=b$,
    -   $a_1a_2\cdots a_k+a_{k+1}a_{k+2}\cdots a_{2k}=b^k-1$.
    
    Nadalje, ako $l$ ima netrivijalni djelitelj $k$ i $l=nk$, tada je $\sum_{i=0}^{n-1}a_{ik+1}a_{ik+2}\cdots a_{(i+1)k}$ višekratnik od $b^k-1$.

??? example "Primjer"
    Za $1/19=0.\overline{052~631~578~947~368~421}=0.\overline{032~745}_{(8)}$ vrijedi:
    
    -   $052~631~578+947~368~421=999~999~999$,
    -   $052+631+578+947+368+421=3\times 999$,
    -   $032_{(8)}+745_{(8)}=777_{(8)}$,
    -   $03_{(8)}+27_{(8)}+45_{(8)}=77_{(8)}$.

??? note "Dokaz"
    Za $a,b,p,l,n,k$ iz teorema lako se vidi $1\leq a<p$, $b>1$ i $(a,p)=(b,p)=1$.
    
    Za cijeli broj $0\leq i<l$ stavimo $f(i)=b^i\cdot a/p-\lfloor b^i\cdot a/p\rfloor$; vrijedi
    
    $$
    0<f(i)=0.\overline{a_{i+1}a_{i+2}\cdots a_{nk}a_1a_2\cdots a_i}<1 \implies 0<pf(i)<p.
    $$
    
    Uočimo da je $pf(i)\in\mathbf{N}_+$ i $pf(i)\equiv ab^i\pmod p$, pa je $pf(i)=ab^i\bmod p$.
    
    Stavimo $S_n=\sum_{i=0}^{n-1}f(ik)=\sum_{i=0}^{n-1}0.\overline{a_{ik+1}a_{ik+2}\cdots a_{nk}a_1a_2\cdots a_{ik}}$; među decimalnim brojevima možemo „razmijeniti” nekoliko znamenaka (na primjer $0.\overline{{\color{Orchid}{14}}{\color{RoyalBlue}{28}}{\color{YellowGreen}{57}}}+0.\overline{{\color{RoyalBlue}{28}}{\color{YellowGreen}{57}}{\color{Orchid}{14}}}+0.\overline{{\color{YellowGreen}{57}}{\color{Orchid}{14}}{\color{RoyalBlue}{28}}}=0.\overline{\color{Orchid}{141414}}+0.\overline{\color{RoyalBlue}{282828}}+0.\overline{\color{YellowGreen}{575757}}=0.\overline{\color{Orchid}{14}}+0.\overline{\color{RoyalBlue}{28}}+0.\overline{\color{YellowGreen}{57}}=14/99+28/99+57/99=1$), pa je
    
    $$
    \begin{aligned}
        S_n&=\sum_{i=0}^{n-1}0.\overline{a_{ik+1}a_{ik+2}\cdots a_{(i+1)k}}\\
        &=\sum_{i=0}^{n-1}a_{ik+1}a_{ik+2}\cdots a_{(i+1)k}/\left(b^k-1\right),
    \end{aligned}
    $$
    
    a odatle
    
    $$
    pS_n=p\sum_{i=0}^{n-1}a_{ik+1}a_{ik+2}\cdots a_{(i+1)k}/\left(b^k-1\right)= \sum_{i=0}^{n-1} \left(ab^{ik}\bmod p\right),
    $$
    
    dakle
    
    $$
    \sum_{i=0}^{n-1}a_{ik+1}a_{ik+2}\cdots a_{(i+1)k}=\left(b^k-1\right)\frac{\sum_{i=0}^{n-1} \left(ab^{ik}\bmod p\right)}{p}.
    $$
    
    Ako $p\mid \left(b^k-1\right)$, uočimo da je
    
    $$
    \left(b^k-1\right)a/p=a_1a_2\cdots a_k.\overline{a_{k+1}a_{k+2}\cdots a_{nk}a_1a_2\cdots a_k}-0.\overline{a_{1}a_{2}\cdots a_{nk}},
    $$
    
    pa vrijedi $a_{k+1}a_{k+2}\cdots a_{nk}a_1a_2\cdots a_k=a_{1}a_{2}\cdots a_{nk}$, odakle $a_1a_2\cdots a_k=a_{k+1}a_{k+2}\cdots a_{2k}=\dots=a_{(n-1)k+1}a_{(n-1)k+2}\cdots a_{nk}$, tj. $0.\overline{a_1a_2\cdots a_l}=0.\overline{a_1a_2\cdots a_k}$, što je u suprotnosti s definicijom $l$; stoga $p\nmid \left(b^k-1\right)$.
    
    Dakle, postoji pozitivan cijeli broj $c=\dfrac{\sum_{i=0}^{n-1} \left(ab^{ik}\bmod p\right)}{p}$ takav da je
    
    $$
    \sum_{i=0}^{n-1}a_{ik+1}a_{ik+2}\cdots a_{(i+1)k}=c\left(b^k-1\right).
    $$

???+ note "Korolar"
    Za gornje $b,n,k,p$ vrijedi
    
    $$
    \sum_{i=0}^{n-1} b^{ik}\equiv 0\pmod p.
    $$

## Poopćeni pozicijski sustavi

U standardnom pozicijskom sustavu baza $b$ uvijek je fiksan pozitivan broj, svaka se znamenka bira među $b$ različitih simbola i prikazuje se nenegativan broj (ne razmatramo decimalnu točku ni predznak). Zapravo postoji još mnogo sustava zapisivanja brojeva sa sličnim obilježjima koji ne zadovoljavaju u potpunosti pravila pozicijskog sustava; takve sustave nazivamo **poopćenim pozicijskim sustavima** ili **nestandardnim pozicijskim brojevnim sustavima** (non-standard positional numeral systems). U nastavku predstavljamo nekoliko uobičajenih poopćenih pozicijskih sustava.

### Bijektivni brojevni sustav

Standardni pozicijski sustav ne uspostavlja bijekciju s brojevima koje prikazuje; na primjer, $1$, $01$ i $001$ prikazuju isti broj[^note1], dok **bijektivni brojevni sustav** (bijective numeral system) uspostavlja bijekciju s brojevima koje prikazuje.

Bijektivni sustav s bazom $k$ ($k\geq 1$) jednoznačno prikazuje broj pomoću skupa znamenaka $\{1,2,\dots,k\}$ po sljedećim pravilima:

1.  prazan niz prikazuje $0$;
2.  neprazan niz $a_n\cdots a_1a_0$ prikazuje broj $a_nk^n+\cdots+a_1k^1+a_0k^0=\sum_{i=0}^n a_ik^i$.

Za pozitivan broj $m$ čiji je zapis u bijektivnom sustavu s bazom $k$ jednak $a_n\cdots a_1a_0$ vrijedi:

$$
\begin{array}{cc}
    a_0=m-q_0k,&q_0=f(m/k),\\
    a_1=q_0-q_1k,&q_1=f(q_0/k),\\
    \vdots&\vdots\\
    a_n=q_{n-1}-q_nk,&q_n=f(q_{n-1}/k)=0,\\
\end{array}
$$

gdje je $f(x)=\lceil x\rceil-1$.

Na primjer, oznake stupaca u Microsoft Excelu koriste bijektivni sustav s bazom $26$.

Među bijektivnim brojevnim sustavima imamo [unarni sustav](https://en.wikipedia.org/wiki/Unary_numeral_system); neprazan niz u unarnom sustavu sastoji se samo od znamenaka $1$, a duljina niza jest broj koji on prikazuje.

Slično kao u odjeljku o [metodi komplemenata](#metoda-komplemenata), u bijektivnom sustavu s bazom $k$, gdje je $k>1$, stavimo $d=k-1$; tada je $\cdots dd=:\overline{d}=\sum_{i=0}^{\infty} dk^i=-1$, a odatle $\overline{d}k=0$, pa ako je zapis $x$ u bijektivnom sustavu s bazom $k$ jednak $a_{n-1}\cdots a_1a_0$, tada je $\overline{d}ka_{n-1}\cdots a_1a_0$ jednako $-x$.

Slijede neka svojstva brojeva u bijektivnom sustavu s bazom $k$:

-   Brojeva duljine $l\geq 0$ ima ukupno $k^l$.
-   Za $k\geq 2$ duljina zapisa broja $n$ u bijektivnom sustavu s bazom $k$ iznosi $\lfloor\log_k (n+1)(k-1)\rfloor$.
-   Za $k\geq 2$, ako zapis broja $n$ u bazi $k$ ne sadrži $0$, tada je njegov zapis u bazi $k$ jednak zapisu u bijektivnom sustavu s bazom $k$.

Kôd za pretvorbu iz bijektivnog sustava s bazom $k$ u dekadski isti je kao za pretvorbu iz baze $k$ u dekadski; slijedi referentna implementacija pretvorbe iz dekadskog u bijektivni sustav s bazom $k$

???+ note "Implementacija"
    ```cpp
    --8<-- "docs/math/code/base/base_1.cpp:from_dec_bi"
    ```

### Sustavi sa znamenkama s predznakom

Neki pozicijski sustavi dopuštaju negativne znamenke, na primjer [balansirani ternarni sustav](./balanced-ternary.md).

### Grayev kod

Glavni članak: [Grayev kod](./gray-code.md)

Grayev kod naziva se i **ciklički binarni kod** ili **reflektirani binarni kod** (reflected binary code, RBC); to je poseban binarni brojevni sustav koji se često koristi pri provjeri podataka.

### Sustavi s nepozitivnom bazom

Znamo da za broj $a_n\cdots a_1a_0$ u bazi $k$ vrijednost koju prikazuje iznosi $\sum_{i=0}^n a_ik^i$; malom izmjenom možemo definirati broj ${a_n\cdots a_1a_0}_{(-k)}$ u bazi $-k$ koji prikazuje $\sum_{i=0}^n a_i(-k)^i$, gdje je $a_n,\dots,a_1,a_0\in \{0,1,\dots,k-1\}$. Na primjer, $12345_{(-10)}=8265_{(10)}$. Takav se sustav naziva [**sustav s negativnom bazom**](https://en.wikipedia.org/wiki/Negative_base) (negative-base system).

Slično možemo definirati [**sustav s kompleksnom bazom**](https://en.wikipedia.org/wiki/Complex-base_system) (complex-base system), npr. [**sustav s bazom $2\mathrm{i}$**](https://en.wikipedia.org/wiki/Quater-imaginary_base) (quater-imaginary base, quater-imaginary numeral system), a možemo definirati i [**sustave s necjelobrojnom bazom**](https://en.wikipedia.org/wiki/Non-integer_base_of_numeration) (non-integer base of numeration) za prikaz realnih brojeva pomoću **$\beta$-razvoja** ($\beta$-expansion) itd.

### Sustavi s mješovitom bazom

U standardnom pozicijskom sustavu baza je svake znamenke fiksna, dok sustav s mješovitom bazom dopušta da svaka znamenka ima različitu bazu. Najčešća primjena sustava s mješovitom bazom jest mjerenje vremena: sati koriste bazu $24$, a minute i sekunde bazu $60$.

Broj koji $a_n\cdots a_1a_0$ prikazuje u bazi $b$ iznosi $\sum_{i=0}^n a_ib^i$, dok u sustavu s mješovitom bazom prikazuje $\sum_{i=0}^n a_i\prod_{j=0}^{i-1}b_j$, gdje je $b_j$ baza znamenke $a_j$.

Na algoritamskim natjecanjima najčešći sustav s mješovitom bazom jest [**faktorijelni brojevni sustav**](https://en.wikipedia.org/wiki/Factorial_number_system) (factorial number system), u kojem se brojevi zapisuju kao ${a_n\cdots a_1a_0}_{~!}$ i prikazuju $\sum_{i=0}^na_i i!$[^note2]. Za primjenu faktorijelnog sustava na algoritamskim natjecanjima vidi [Lehmerov kod/Cantorov razvoj](../permutation.md#排名).

???+ note "Implementacija (iz dekadskog u faktorijelni sustav)"
    ```cpp
    --8<-- "docs/math/code/base/base_1.cpp:from_dec_factorial"
    ```

???+ note "Implementacija (iz faktorijelnog sustava u dekadski)"
    ```cpp
    --8<-- "docs/math/code/base/base_1.cpp:to_dec_factorial"
    ```

## Implementacija u C++-u

Za nenegativne brojeve C++ cjelobrojni literal zapisuje kao `<prefiks><znamenke><sufiks>`, pri čemu `<znamenke>` i `<sufiks>` mogu biti prazni. `<sufiks>` označava tip literala, npr. `u` ili `U` označava da je literal `unsigned`, `l` ili `L` da je `long` itd. Za `<prefiks>`:

-   kad je `<prefiks>` `0x` ili `0X`, riječ je o heksadekadskom literalu i znakovi u `<znamenke>` mogu biti samo iz skupa `0, 1, 2, 3, 4, 5, 6, 7, 8, 9, a, A, b, B, c, C, d, D, e, E, f, F`. Na primjer, `0x1234ABCD` je $\text{1234ABCD}_{(16)}=305~441~741$;
-   kad je `<prefiks>` `0`, riječ je o oktalnom literalu i znakovi u `<znamenke>` mogu biti samo iz skupa `0, 1, 2, 3, 4, 5, 6, 7`. Na primjer, `01234567` je $1234567_{(8)}=342391$;[^note3]
-   kad je `<prefiks>` `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8` ili `9`, riječ je o dekadskom literalu i znakovi u `<znamenke>` mogu biti samo iz skupa `0, 1, 2, 3, 4, 5, 6, 7, 8, 9`;
-   od C++14, kad je `<prefiks>` `0b` ili `0B`, riječ je o binarnom literalu i znakovi u `<znamenke>` mogu biti samo iz skupa `0, 1`. Na primjer, `0b11001010` je $11001010_{(2)}=202$.

## Literatura i napomene

-   [Positional notation - Wikipedia](https://en.wikipedia.org/wiki/Positional_notation)
-   [Method of complements - Wikipedia](https://en.wikipedia.org/wiki/Method_of_complements)
-   [Non-standard positional numeral systems - Wikipedia](https://en.wikipedia.org/wiki/Non-standard_positional_numeral_systems)
-   [Bijective numeration - Wikipedia](https://en.wikipedia.org/wiki/Bijective_numeration)
-   [Midy's theorem - Wikipedia](https://en.wikipedia.org/wiki/Midy%27s_theorem)
-   [N3472 - Binary Literals in the C++ Core Language](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2012/n3472.pdf)

[^note1]: Znamenke $0$ ispred najviše znamenke različite od $0$ nazivamo [**vodećim nulama**](https://en.wikipedia.org/wiki/Leading_zero) (leading zero). Slično možemo definirati [**završne nule**](https://en.wikipedia.org/wiki/Trailing_zero) (trailing zero).

[^note2]: Baza znamenke $a_i$ jest $i+1$, $0\leq a_i\leq i$. Uočimo da je $(n+1)!-n!=n\cdot n!$, pa je zapis broja u faktorijelnom sustavu jedinstven ako se uklone vodeće nule.

[^note3]: `0` je oktalni literal.

[^note4]: U nekim se krajevima za decimalnu točku koristi „$,$”.

[^note5]: Za $a=1$ niz prostih brojeva koji u dekadskom sustavu zadovoljavaju taj uvjet jest [A028416](https://oeis.org/A028416).
