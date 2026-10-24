---
title: Slučajni brojevi
---

## Pregled

Preduvjet za korištenje randomiziranih tehnika jest mogućnost brzog generiranja slučajnih brojeva. Ovaj članak predstavlja uobičajene metode generiranja slučajnih brojeva.

### Slučajni i pseudoslučajni brojevi

Nema smisla reći da je jedan pojedinačni broj „slučajan”, pa u nastavku podrazumijevamo da govorimo o „nizu slučajnih brojeva”; čak i kad spominjemo „slučajni broj”, mislimo na „element niza slučajnih brojeva”.

Računski procesi današnjih računala deterministički su, pa je nemoguće samo pomoću algoritma generirati niz slučajnih brojeva koji bi bio uistinu **nepredvidiv** i **neponovljiv**.

Međutim, u velikoj većini slučajeva ne trebamo tako jaku slučajnost, nego nam je dovoljno da generirani niz statistički ima razna svojstva niza slučajnih brojeva (npr. uniformnu distribuciju, međusobnu nezavisnost itd.). Takav niz zovemo nizom **pseudoslučajnih brojeva**.

Primjeri primjene slučajnih i pseudoslučajnih brojeva u stvarnom životu i u algoritmima:

-   Pri uzorkovanju u anketama obično su dovoljni pseudoslučajni brojevi. Razlog je to što nas ionako zanimaju samo statistička svojstva.
-   U računalnoj sigurnosti često su potrebni jači slučajni brojevi (od upravo spomenutih pseudoslučajnih). Razlog je to što napadač može iskoristiti predvidivost.
-   Randomiziranim algoritmima koji se koriste u OI/ICPC-u gotovo uvijek su dovoljni pseudoslučajni brojevi. Razlog je to što ti algoritmi uvođenjem slučajnih brojeva obično unose vjerojatnost u analizu složenosti i time smanjuju složenost. To u biti i dalje koristi samo statistička svojstva slučajnih brojeva.
-   Neki randomizirani algoritmi (npr. [Moserov algoritam](https://en.wikipedia.org/wiki/Algorithmic_Lov%C3%A1sz_local_lemma)) koriste svojstva slučajnih brojeva povezana s entropijom, pa moraju koristiti prave slučajne brojeve.

## Metode generiranja slučajnih brojeva

### `rand`

Služi za generiranje pseudoslučajnih brojeva; nedostatak mu je što je prilično spor. Za korištenje je potrebno `#include<cstdlib>`.

Poziv funkcije `rand()` vraća slučajan nenegativan cijeli broj iz `[0,RAND_MAX]`, gdje je `RAND_MAX` makro iz standardne biblioteke; na Linuxu je `RAND_MAX` jednak $2^{31}-1$. Veličinu generiranih brojeva možemo ograničiti uzimanjem ostatka.

Za korištenje `rand()` potrebno je sjeme (seed) slučajnih brojeva; funkcijom `srand(seed)` sjeme se može promijeniti u `seed`, a naravno može se i ne inicijalizirati.

Ako se isti program dvaput pokrene s istim `seed`, na istom računalu i s istim prevoditeljem, dobiveni slučajni rezultati bit će jednaki.

Jedna je mogućnost koristiti trenutno sistemsko vrijeme kao sjeme: `srand(time(nullptr))`.

??? warning "Upozorenje"
    Na sustavu `Windows` raspon vrijednosti koje vraća `rand()` jest $\left[0,2^{15}\right)$ (tj. `RAND_MAX` je jednak $2^{15}-1$); kad treba generirati brojeve koji nisu manji od $2^{15}$, preporučuje se za veće slučajne brojeve koristiti `(rand() << 15 | rand())`.

O slučajnosti `rand()` i `rand()%n`:

-   Standard C/C++ ne propisuje ništa o kvaliteti slučajnih brojeva koje generira `rand()`, ni u kojem pogledu.
-   Implementacija `rand()` u GCC-u jamči osnovna svojstva poput uniformnosti distribucije, ali ima očite nedostatke poput kratkog perioda nižih bitova. (Primjerice, na autorovu računalu period niza koji generira `rand()%2` iznosi otprilike $2\cdot 10^6$.)
-   Čak i ako pretpostavimo da je `rand()` uniformno slučajan, `rand()%n` ne jamči uniformnost, jer se brojevi iz `[0,n)` mogu pojavljivati različit broj puta među `0%n,1%n,...,RAND_MAX%n`. Za postupak koji strogo jamči uniformnost pogledajte [Daniel Lemire, Fast Random Integer Generation in an Interval](https://arxiv.org/abs/1805.10941).

### Predefinirani generatori slučajnih brojeva

Definirano je nekoliko posebnih popularnih algoritama. Ako nije drukčije navedeno, svi su definirani u zaglavlju `<random>`.

??? warning "Upozorenje"
    Predefinirani generatori slučajnih brojeva dostupni su od standarda C++11[^ref2].

#### Mersenne Twister

Mersenne Twister predložili su Matsumoto i Nishimura 1998. godine[^ref3]; ime je dobio po tome što jedna njegova implementacija, MT19937, ima period duljine Mersenneova prostog broja $M_{19937} = 2^{19937} - 1$.

Od C++11 predložak klase `std::mersenne_twister_engine` implementira generator slučajnih brojeva zasnovan na gornjoj metodi. Budući da je njegovo korištenje vrlo složeno, u praksi se obično koriste specijalizacije tog predloška: `std::mt19937` i `std::mt19937_64`. Njihova je prednost visoka kvaliteta slučajnih brojeva i znatno veća brzina od `rand()`.

`mt19937` zasnovan je na 32-bitnom Mersenne Twisteru, koji su Matsumoto i Nishimura predložili 1998. godine[^ref3]; to je klasa generatora slučajnih brojeva s istom ulogom kao `rand()`, a raspon slučajnih brojeva jednak je rasponu tipa `unsigned int`. Za korištenje jednostavno njime definiramo generator slučajnih brojeva: `mt19937 myrand(seed)`; `seed` se može izostaviti, a tada se koristi zadano sjeme. Klasa preopterećuje `operator()`, pa kad treba generirati slučajan broj, dovoljno je pozvati `myrand()` i vraća se slučajan broj.

Sličan je generator `mt19937_64`, zasnovan na 64-bitnom Mersenne Twisteru koji su Matsumoto i Nishimura predložili 2000. godine; koristi se jednako kao `mt19937`, ali je raspon slučajnih brojeva proširen na raspon tipa `unsigned long long`.

??? note "Primjer koda"
    ```cpp
    --8<-- "docs/misc/code/random/random_1.cpp:core"
    ```

#### Linearni kongruentni generator slučajnih brojeva

Linearni kongruentni generator slučajnih brojeva (skraćeno LCG) predložili su Thomson i Rotenberg 1958. godine. Računa se prema sljedećoj formuli, gdje su $A, C, M$ predefinirane konstante:

$$
s_i \equiv \begin{cases}
\operatorname{seed} & i = 0 \\
s_{i-1} \times A + C & i \ge 1
\end{cases}\pmod{M}
$$

Od C++11 predložak klase `std::linear_congruential_engine` implementira generator slučajnih brojeva zasnovan na gornjoj metodi, s parametrima predloška:

```cpp
template <class UIntType, UIntType A, UIntType C, UIntType M>
class linear_congruential_engine;
```

Ovdje `UIntType` označava tip od $s$, a slijede tri konstante.

Zatim su Lewis, Goodman i Miller 1969. predložili da se uzme $A = 7^{5} = 16807$, $C = 0$, $M = 2^{31} - 1 = 2147483647$; tada algoritam postiže gotovo maksimalan period $2^{31} - 2$ za taj modul (jer je $16807$ [primitivni korijen](../math/number-theory/primitive-root.md) po tom modulu) i ima relativno dobra statistička svojstva.

Potom su 1988. Park i Miller LCG s tim parametrima prihvatili kao „minimalni standard”, upravo zato što je njegova implementacija iznimno jednostavna, razumljiva, učinkovita i relativno dobre kvalitete. Naposljetku su 1993. Park, Miller i Stockmeyer promijenili parametar $A$ u $48271$, što je postalo noviji „minimalni standard”. Obje inačice „minimalnog standarda” predefinirane su u C++11 kao specijalizacije `linear_congruential_engine`, redom `minstd_rand0` i `minstd_rand`. Konkretno:

-   Za `minstd_rand0` tip od $s_i$ jest `std::uint_fast32_t`, $A$ je $16807$, $C$ je $0$, a $M$ je $2147483647$.

-   Za `minstd_rand` tip od $s_i$ jest `std::uint_fast32_t`, $A$ je $48271$, $C$ je $0$, a $M$ je $2147483647$.

Korištenje je također jednostavno. Prvo definiramo `std::minstd_rand myrand(seed);`, gdje je `seed` sjeme, a ako se izostavi, zadana je vrijednost $1$. Zatim pozivom `myrand()` dobivamo slučajan broj.

Ako treba prilagođeni generator slučajnih brojeva ovog oblika, a $A, C, M$ nisu konstante, može se razmotriti i ručna implementacija. Ta je metoda jednostavna za implementaciju, ali generirani slučajni niz ima relativno kratak period (period je najviše $M$, no u većini slučajeva kraći od $M$).

??? note "Referentna implementacija"
    ```cpp
    --8<-- "docs/misc/code/random/random_2.cpp"
    ```

### Adapteri generatora slučajnih brojeva

Na temelju predefiniranih generatora slučajnih brojeva mogu se dodatnim omatanjem dobiti novi generatori slučajnih brojeva. Konkretna imena klasa i način korištenja potražite u popisu [Pseudo-random number generation – Random number engine adaptors](https://en.cppreference.com/w/cpp/numeric/random#Random_number_engine_adaptors).

Sljedeći kod pomoću `std::independent_bits_engine` omata izlaz generatora `std::minstd_rand`.

```cpp
--8<-- "docs/misc/code/random/random_3.cpp"
```

### Nedeterministički generator uniformno distribuiranih slučajnih cijelih brojeva

`random_device` je hardverski zasnovan generator uniformno distribuiranih slučajnih brojeva koji može brzo generirati slučajne brojeve **dok se ne iscrpi spremnik entropije**. Klasa je definirana u C++11 i zahtijeva zaglavlje `random`. Budući da nakon iscrpljenja spremnika entropije performanse naglo padaju, preporučuje se ovom metodom generirati sjeme za pseudoslučajne generatore poput `mt19937`, a ne same slučajne brojeve.

`random_device` je nedeterministički generator uniformno slučajnih bitova, iako je implementaciji dopušteno da ga, ako nedeterminističko generiranje slučajnih brojeva nije podržano, ostvari pseudoslučajnim pogonom. Autor dosad nije primio izvještaje da evaluacijska računala NOIP-a ne podržavaju hardverski zasnovano generiranje uniformno distribuiranih slučajnih brojeva. Ipak, iz opreza, preporučuje se ovaj algoritam koristiti za generiranje sjemena slučajnih brojeva.

Referentni kod slijedi.

```cpp
--8<-- "docs/misc/code/random/random_4.cpp"
```

Mogući izlaz je sljedeći.

```plain
0 : ********************
1 : *******************
2 : ********************
3 : ********************
4 : ********************
5 : *******************
6 : ********************
7 : ********************
8 : *******************
9 : ********************
```

### Distribucije slučajnih brojeva

Ovdje su predstavljeni generatori slučajnih brojeva koji zahtijevaju da generirani slučajni brojevi slijede određenu distribuciju, npr. [diskretnu uniformnu distribuciju](https://en.wikipedia.org/wiki/Discrete_uniform_distribution), [Bernoullijevu distribuciju](https://en.wikipedia.org/wiki/Bernoulli_distribution), [binomnu distribuciju](https://en.wikipedia.org/wiki/Binomial_distribution), [geometrijsku distribuciju](https://en.wikipedia.org/wiki/Geometric_distribution), [standardnu normalnu (Gaussovu) distribuciju](https://en.wikipedia.org/wiki/Normal_distribution).

Konkretna imena klasa potražite u popisu [Pseudo-random number generation – Random number distributions](https://en.cppreference.com/w/cpp/numeric/random#Random_number_distributions).

Sljedeći program simulira kocku sa šest strana.

```cpp
--8<-- "docs/misc/code/random/random_5.cpp:header"
--8<-- "docs/misc/code/random/random_5.cpp:real-using"
--8<-- "docs/misc/code/random/random_5.cpp:fake-using"
--8<-- "docs/misc/code/random/random_5.cpp:main"
```

### Ostale metode implementacije

Ponekad trebamo implementirati vlastiti generator slučajnih brojeva. Slijede neke često korištene metode generiranja slučajnih brojeva.

#### Xorshift

Obitelj generatora slučajnih brojeva Xorshift predložio je George Marsaglia 2003. godine; zasniva se uglavnom na jednoj operaciji: XOR-u broja s njegovim pomakom. U algoritamskim natjecanjima često se koriste dvije inačice, `xorshift32` i `xorshift64`:

```cpp
--8<-- "docs/misc/code/random/random_6.cpp:core"
```

Način korištenja sličan je većini prethodno predstavljenih generatora slučajnih brojeva: prvo definiramo generator `xorshift32 rng32(seed)` ili `xorshift64 rng64(seed)`, gdje je `seed` sjeme, a ako se izostavi, koristi se zadano sjeme; zatim pozivom `rng32()` ili `rng64()` dobivamo slučajan broj. Kad sjeme nije $0$, ova dva generatora imaju period $2^{32} - 1$ odnosno $2^{64} - 1$; budući da je njihova implementacija iznimno jednostavna, često se natjecateljima daju zajedno sa sjemenom kako bi sami generirali velike ulazne podatke i time smanjili trošak ulaza/izlaza.

#### SplitMix

Obitelj generatora slučajnih brojeva SplitMix predložili su Steele, Lea i Flood 2014. godine, a primijenjena je u klasi `java.util.SplittableRandom` u Javi 8. U svijetu algoritamskih natjecanja najčešće se koristi inačica `splitmix64`:

```cpp
--8<-- "docs/misc/code/random/random_7.cpp:core"
```

Njezina je glavna upotreba ponovno hashiranje već izračunate hash-vrijednosti, kako netko pažljivo konstruiranim podacima ne bi srušio hash-tablicu i izazvao prekoračenje vremenskog ograničenja:

```cpp
--8<-- "docs/misc/code/random/random_8.cpp:core"
```

Može se koristiti i za generiranje slučajnih brojeva: prvo definiramo `splitmix64 rng64(seed)`, gdje je `seed` sjeme, a ako se izostavi, koristi se zadano sjeme; zatim pozivom `rng64()` dobivamo slučajan broj. Tada je prilično očito da ova funkcija ima period $2^{64}$ (jer su sve velike konstante neparne, pa $x$ ima period $2^{64}$, a sve kasnije operacije nad $z$ potpuno su reverzibilne). To također znači da, čak i ako ne možete zapamtiti gornje velike parametre, možete jednostavno napisati nekoliko proizvoljnih dovoljno velikih neparnih brojeva u kombinaciji s XOR-om i pomakom udesno te postići sličan učinak.

#### Fibonaccijev generator slučajnih brojeva s kašnjenjem

Niz slučajnih brojeva $\{R_i\}$ generira se sljedećom formulom (gdje je $0 < j < k$):

$$
R_i \equiv R_{i-j} \star R_{i-k} \bmod P
$$

Ovdje se za $P$ obično uzima potencija broja $2$ (često $2^{32}$ ili $2^{64}$), a $\star$ označava binarni operator, koji može biti zbrajanje, oduzimanje, množenje ili XOR.

U usporedbi s tradicionalnim linearnim kongruentnim generatorima slučajnih brojeva ova metoda ima dulji period, ali na njezinu slučajnost znatno utječu početni uvjeti.

??? note "Referentna implementacija"
    ```cpp
    --8<-- "docs/misc/code/random/random_9.cpp:core"
    ```

Vrijedi spomenuti da je u C++11 `std::subtract_with_carry_engine` jedna od implementacija ove vrste generatora slučajnih brojeva, a `std::ranlux24_base` i `std::ranlux48_base` specijalizacije su tog predloška klase, dok se `std::ranlux24` i `std::ranlux48` dobivaju tako da se na prethodne primijeni adapter `std::discard_block_engine`. Međutim, danas se njihovo korištenje obično više ne preporučuje.

## Randomizirani algoritmi

U nastavku predstavljamo neke randomizirane algoritme definirane u standardu C++ koji se oslanjaju na generiranje slučajnih brojeva.

### `random_shuffle`

`std::random_shuffle` uveden je u C++98 i služi za slučajno miješanje zadanog niza. Za korištenje je potrebno `#include<algorithm>`; uobičajena je implementacija [Fisher–Yatesov algoritam](https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle).

Pri korištenju dovoljno je predati pokazivače ili iteratore na početak i kraj zadanog raspona (zatvoren slijeva, otvoren zdesna): `std::random_shuffle(first, last)` ili `std::random_shuffle(first, last, myrand)`.

Generator slučajnih brojeva koji se interno koristi zadano je `rand()`. Naravno, može se predati i prilagođeni generator slučajnih brojeva.

O slučajnosti `random_shuffle`:

-   Standard C++ zahtijeva da `random_shuffle` **s jednakom vjerojatnošću** slučajno odabere među svim mogućim permutacijama, ali zadana standardna biblioteka GCC-a[^note1], libstdc++, to **ne** provodi strogo.
-   Jedan od uzroka nedostatka slučajnosti `random_shuffle` u GCC-u jest to što koristi izraz oblika `rand()%n`. Kao što je ranije rečeno, tako generirani brojevi nisu uniformno slučajni cijeli brojevi.
-   Drugi je uzrok ograničen raspon vrijednosti `rand()`. Ako duljina predanog raspona premašuje `RAND_MAX`, neke se permutacije **ne mogu** nikako dobiti[^ref1].

??? warning "Upozorenje"
    `random_shuffle` zastario je (deprecated) u standardu C++14 i uklonjen u standardu C++17.

### `shuffle`

`std::shuffle` uveden je u C++11 i ima istu ulogu kao `random_shuffle`. Za korištenje je potrebno `#include<algorithm>`.

Razlika je u tome što se obavezno mora koristiti prilagođeni generator slučajnih brojeva: `std::shuffle(first, last, myrand)`.

Implementacija `shuffle` u GCC-u[^note1] u skladu je sa zahtjevima standarda C++, tj. s jednakom vjerojatnošću slučajno odabire među svim mogućim permutacijama.

Slijedi generator ulaznih podataka napisan pomoću `rand()` i `random_shuffle()`. Generira male slučajne ulazne podatke za zadatak [„ZJOI2012” 灾难 (Katastrofa)](https://www.luogu.com.cn/problem/P2597).

```cpp
--8<-- "docs/misc/code/random/random_10.cpp:header"
--8<-- "docs/misc/code/random/random_10.cpp:real-using"
--8<-- "docs/misc/code/random/random_10.cpp:fake-using"
--8<-- "docs/misc/code/random/random_10.cpp:main"
```

Slijedi isti generator ulaznih podataka napisan pomoću `mt19937` i `shuffle()`.

```cpp
--8<-- "docs/misc/code/random/random_11.cpp:header"
--8<-- "docs/misc/code/random/random_11.cpp:real-using"
--8<-- "docs/misc/code/random/random_11.cpp:fake-using"
--8<-- "docs/misc/code/random/random_11.cpp:main"
```

Slijedi implementacija slučajne permutacije prvih deset pozitivnih cijelih brojeva.

```cpp
--8<-- "docs/misc/code/random/random_12.cpp:header"
--8<-- "docs/misc/code/random/random_12.cpp:real-using"
--8<-- "docs/misc/code/random/random_12.cpp:fake-using"
--8<-- "docs/misc/code/random/random_12.cpp:main"
```

### `sample`

`std::sample` uveden je u C++17 i služi za slučajan odabir $n$ elemenata iz niza; glavna razlika u odnosu na uzimanje prvih $n$ elemenata nakon `shuffle` jest to što odabrani elementi u izlazu zadržavaju svoj relativni redoslijed. Uobičajena je implementacija [uzorkovanje spremnikom (reservoir sampling)](https://en.wikipedia.org/wiki/Reservoir_sampling).

Koristi se kao `std::sample(first, last, dest, n, myrand)`, gdje `[first, last)` označava raspon iz kojeg se uzorkuje, `[dest, dest + n)` mjesto na koje se ispisuje, a `myrand` zadani generator slučajnih brojeva.

Slijedi implementacija slučajnog odabira 4 od 11 velikih slova.

```cpp
--8<-- "docs/misc/code/random/random_13.cpp:header"
--8<-- "docs/misc/code/random/random_13.cpp:real-using"
--8<-- "docs/misc/code/random/random_13.cpp:fake-using"
--8<-- "docs/misc/code/random/random_13.cpp:main"
```

## Literatura i bilješke

[^ref1]: [Don't use rand(): a guide to random number generators in C++](https://codeforces.com/blog/entry/61587)

[^ref2]: [Pseudo-random number generation - cppreference.com](https://en.cppreference.com/w/cpp/numeric/random#Predefined_random_number_generators)

[^ref3]: [Mersenne Twister algorithm](https://en.wikipedia.org/wiki/Mersenne_Twister)

[^note1]: Inačica GCC 9.2.0
