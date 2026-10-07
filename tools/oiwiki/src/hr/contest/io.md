---
title: Optimizacija učitavanja i ispisa
---

Ovaj članak opisuje kako optimizirati I/O temeljen na tokovima (streams) i I/O u stilu C-a.

???+ note "Napomena"
    Stvarna brzina I/O-a temeljenog na tokovima i I/O-a u stilu C-a donekle se mijenja ovisno o okruženju (npr. prevoditelju, operacijskom sustavu i hardverskim specifikacijama). Želite li dublju analizu, oslonite se na rezultate eksperimenata. Pritom pazite na kontrolu varijabli u eksperimentu, kako utjecaj više varijabli ne bi doveo do pogrešnih zaključaka.

## I/O temeljen na tokovima

Za I/O temeljen na tokovima (kao što su `std::cin` i `std::cout`) najčešće su optimizacije isključivanje sinkronizacije s C-ovim tokovima i razdvajanje ulaznog i izlaznog toka.

### Isključivanje sinkronizacije

Funkcijom [`std::ios::sync_with_stdio(false)`](https://en.cppreference.com/w/cpp/io/ios_base/sync_with_stdio) isključuje se sinkronizacija s C-ovim tokovima. Radi kompatibilnosti s C-om, to jest da bi program koji istodobno koristi `printf` i `std::cout` radio bez zbrke, C++ te dvije vrste tokova sinkronizira. Sinkronizirani C++ tokovi zajamčeno su sigurni za rad s dretvama (thread-safe).

To je zapravo konzervativna mjera koju C++ poduzima radi kompatibilnosti. Kad je sinkronizacija uključena, C++ tok pri svakoj I/O operaciji tu operaciju odmah primjenjuje na odgovarajući C-ov međuspremnik, a ako kôd uopće ne koristi I/O u stilu C-a, ta je operacija suvišna. Zato se prije I/O operacija sinkronizacija s C-ovim tokovima može isključiti, ali nakon toga treba paziti da se u ostatku koda ne koriste istodobno `std::cin` i `scanf` niti istodobno `std::cout` i `printf`; smiju se, međutim, istodobno koristiti `std::cin` i `printf`, kao i `scanf` i `std::cout`.

### Razdvajanje tokova

Funkcijom [`tie()`](https://en.cppreference.com/w/cpp/io/basic_ios/tie) razdvaja se ulazni tok od izlaznog.

Prema zadanim postavkama `std::cin` je vezan uz `&std::cout`, pa se pri svakom formatiranom unosu poziva `std::cout.flush()` koji prazni izlazni međuspremnik, što povećava opterećenje I/O-a. Pozivom `std::cin.tie(nullptr)` ta se veza može ukloniti i tako dodatno ubrzati izvođenje.

???+ warning "Napomena"
    Pritom se argument ne smije izostaviti i napisati `std::cin.tie()`; to ne razdvaja tokove, nego vraća izlazni tok vezan uz `std::cin`. Također nije potrebno pozvati `std::cout.tie(nullptr)`, jer prema zadanim postavkama nijedan drugi izlazni tok nije vezan uz `std::cout`.

### Implementacija

```cpp
std::ios::sync_with_stdio(false);
std::cin.tie(nullptr);
```

???+ note "Napomena"
    Nakon što se obave obje gornje operacije, program mora ručno pozvati `flush` kako bi sadržaj koji `std::cout` ispisuje zajamčeno bio prikazan prije `std::cin`. Razlog je to što se u tom slučaju pri pozivu `std::cin` međuspremnik `std::cout` ne prazni automatski. Na primjer:
    
    ```cpp
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::cout << "Please input your name: "
              << std::flush;  // ili: std::endl;
                              // jer svaki poziv std::endl prazni (flush) izlazni međuspremnik, a \n
                              // ne.
    // Ako se std::flush izostavi, poruka se neće prikazati prije unosa imena
    std::cin >> name;
    ```

## I/O u stilu C-a

I `scanf` i `printf` još se mogu ubrzati; sve se metode ubrzanja temelje na pretvorbi između cijelih brojeva i stringova.

???+ note "Napomena"
    Optimizacije učitavanja i ispisa opisane na ovoj stranici odnose se na cjelobrojne podatke. Optimizacija učitavanja i ispisa brojeva s pomičnim zarezom vrlo je složena; za učitavanje vidi [algoritam Bellerophon](https://dl.acm.org/doi/10.1145/93542.93557), a za ispis [algoritam Ryū](https://dl.acm.org/doi/10.1145/3192366.3192369).

### Oblikovanje implementacije

???+ note "Napomena"
    Ovdje opisane optimizacije usmjerene su na brži I/O, dok se pri pretvorbi podataka koriste naivne metode koje ne iskorištavaju u potpunosti mogućnosti hardvera. Danas velika većina procesora arhitekture x86 podržava skup instrukcija AVX2, pa se SIMD-om može ubrzati pretvorba između cijelih brojeva i stringova. Funkcije standardne biblioteke ne koriste SIMD optimizacije; npr. [implementacija](https://github.com/gcc-mirror/gcc/blob/releases/gcc-14.3.0/libstdc%2B%2B-v3/include/bits/charconv.h#L81) u libstdc++-u pretvara po dvije uzastopne znamenke odjednom, i to tablicom pretvara u znakove, pa optimizacija samog postupka pretvorbe također može donijeti dobit. U natjecateljskom okviru, međutim, optimizacije spomenute u ovom članku dostatne su za veliku većinu situacija.

#### Optimizacija učitavanja

Svaki cijeli broj sastoji se od predznaka i znamenaka, a predznak uvijek prethodi znamenkama, pa se prvo učitava predznak. Kod predznaka se `+` za pozitivne brojeve obično izostavlja i ne utječe na vrijednost koju predstavljaju znamenke iza njega, dok se `-` ne smije izostaviti, pa ga treba provjeriti. Ako ulaz ne sadrži negativne brojeve, ta se provjera može izostaviti. Dio sa znamenkama sadrži samo znamenke od 0 do 9, pa kad se učita znak koji ne može biti dio cijelog broja (obično razmak), može se zaključiti da je učitavanje tog broja završilo.

Budući da se pri učitavanju znamenke čitaju slijeva nadesno, za pretvorbu u cijeli broj može se iskoristiti upravo Hornerov algoritam. Zato se cijeli postupak pretvorbe može spojiti s učitavanjem.

Pri učitavanju znamenaka treba provjeriti je li učitani znak dekadska znamenka. Može se jednostavno upotrijebiti uvjet `ch >= '0' && ch <= '9'` ili funkcija [`isdigit()`](https://en.cppreference.com/w/cpp/string/byte/isdigit).

#### Optimizacija ispisa

Pri ispisu cijeli broj treba pretvoriti u string; obično se koristi naivni algoritam, tj. znamenke broja računaju se izravno od najniže prema najvišoj, pretvore u znakove i ispišu obrnutim redoslijedom.

### Pojedinosti implementacije

#### Problem cjelobrojnog prekoračenja

U implementaciji treba paziti na cjelobrojno prekoračenje (overflow). Na primjer, nespretno uzimanje suprotnog broja u optimizaciji ispisa dovodi do toga da najmanja vrijednost tipa nakon promjene predznaka premaši najveću vrijednost koju taj tip može prikazati, što može uzrokovati pogrešan ispis. Slično prekoračenje može nastati i pri učitavanju najmanje vrijednosti tipa, ali u tom slučaju učitani podatak možda neće biti pogrešan, jer vrijednost dobivena prekoračenjem može biti jednaka stvarnoj unesenoj vrijednosti.

Prekoračenje predznačenih cijelih brojeva nedefinirano je ponašanje; u implementaciji se gornji problem može izbjeći pomoću svojstva da se u C-u dijeljenje negativnih cijelih brojeva zaokružuje prema nuli. Ako, međutim, ne treba učitavati ni ispisivati negativne brojeve, ili se najmanja vrijednost tipa ne može pojaviti na ulazu ni izlazu, taj se problem neće pojaviti.

#### Povećanje općenitosti implementacije

Ako program koristi cjelobrojne varijable više tipova, možda će trebati implementirati više ulazno-izlaznih funkcija iste logike, a različitih tipova. Tada se u C++-u pomoću [`template`](https://en.cppreference.com/w/cpp/language/templates.html) može ostvariti optimizacija ulaza i izlaza za sve cjelobrojne tipove. Na primjer, prema standardu C++11 može se upotrijebiti

```cpp
template <typename T>
typename std::enable_if<std::is_integral<T>::value &&
                        std::is_signed<T>::value>::type
read(T &x);
```

ili prema standardu C++20

```cpp
template <std::signed_integral T>
void read(T &x);
```

za definiranje funkcije.

Radi lakšeg čitanja, implementacije u nastavku pretpostavljaju da treba učitavati samo cijele brojeve tipa `int`; one su dostatne za potrebe većine zadataka.

### Implementacija

Uobičajene implementacije razlikuju se samo u funkcijama za učitavanje i ispis koje koriste, dok je logika pretvorbe cijelih brojeva ista. U nastavku su predstavljene prema funkcijama za učitavanje i ispis koje koriste.

#### Implementacija pomoću `getchar` i `putchar`

Ključni dio koda je sljedeći.

```cpp
--8<-- "docs/contest/code/io/io_1.cpp:core"
```

#### Implementacija pomoću `fread` i `fwrite`

Pomoću `fread` i `fwrite` može se ostvariti još brže učitavanje i ispis. Njihovi su potpisi sljedeći.

```cpp
std::size_t fread(void* buffer, std::size_t size, std::size_t count,
                  std::FILE* stream);
std::size_t fwrite(const void* buffer, std::size_t size, std::size_t count,
                   std::FILE* stream);
```

Na primjer, `fread(Buf, 1, SIZE, stdin)` znači: sa standardnog ulaza učitaj `SIZE` blokova veličine 1 bajt u `Buf`. Povratna vrijednost označava koliko je bajtova uspješno učitano.

Budući da `fread` i `fwrite` čitaju i pišu u cijelim blokovima, brži su od `getchar()` i `putchar()`. Ako je međuspremnik dovoljno velik, cijela se datoteka može učitati odjednom. Ako međuspremnik nije dovoljno velik, treba čitati više puta kako bi se učitao cijeli ulaz. Da bi se to ostvarilo, dovoljno je ponovno definirati `getchar`.

```cpp
char buf[1 << 20], *p1, *p2;
#define gc()                                                               \
  (p1 == p2 && (p2 = (p1 = buf) + fread(buf, 1, 1 << 20, stdin), p1 == p2) \
       ? EOF                                                               \
       : *p1++)
```

Ispis je sličan učitavanju: sadržaj za ispis prvo se stavi u međuspremnik, a na kraju se pomoću `fwrite` sadržaj međuspremnika ispiše odjednom.

Ključni dio koda je sljedeći.

```cpp
--8<-- "docs/contest/code/io/io_2.cpp:core"
```

Pri upotrebi ove metode treba paziti:

-   Kad je prekidač za ispravljanje (debug) isključen, koriste se `fread()` i `fwrite()`, a pri izlasku se automatski u destruktoru izvršava `fwrite()`. Kad je prekidač uključen, koriste se `getchar()` i `putchar()`, što olakšava ispravljanje.
-   Želite li čitati i pisati u datoteke, prije svih čitanja i pisanja treba dodati `freopen()`.

#### Implementacija pomoću `mmap`

`mmap` je sistemski poziv Linuxa koji datoteku odjednom preslikava u memoriju, slično memorijskom području na koje se može pokazivati pokazivačem, i u nekim je situacijama brži. Njegov je potpis sljedeći:

```c
void *mmap(void addr[.length], size_t length, int prot, int flags, int fd,
           off_t offset);
```

???+ warning "Napomena"
    `mmap` se ne može koristiti u okruženju Windows (npr. na sustavima za ocjenjivanje Codeforcesa i HDU-a), a ne preporučuje se ni na službenim natjecanjima. Zapravo je `fread` već dovoljno brz, a ako se `mmap`-om opetovano čita mali dio datoteke, trošak jednog preslikavanja u memoriju i obrade promašaja stranica (page faults) u jezgri daleko je veći od troška `fread`-a.

Prvo treba dobiti opisnik datoteke `fd`, zatim `fstat`-om dobiti veličinu datoteke, a potom `mmap`-om dobiti pokazivač `*pc` na datoteku preslikanu u memoriju. Nakon toga se za čitanje datoteke umjesto `getchar()` može izravno koristiti `*pc++`.

Ako treba čitati sa standardnog ulaza, `fd` se može postaviti na `0`. **Međutim, upotreba mmap-a na standardnom ulazu krajnje je opasna, a usto se ne može unositi s terminala; može se datoteku preusmjeriti na standardni ulaz.**

???+ note "Primjer: [Luogu P10815 „Predložak” Brzo učitavanje](https://www.luogu.com.cn/problem/P10815)"
    Učitajte $n$ cijelih brojeva iz raspona $[-n, n]$, zbrojite ih i ispišite zbroj. Pritom je $n \leq 10^8$. Podaci jamče da za svaki prefiks niza zbroj tog prefiksa stane u $32$-bitni predznačeni cijeli broj.

Referentni kôd je sljedeći.

```cpp
--8<-- "docs/contest/code/io/io_3.cpp"
```

## Literatura

[cin.tie 与 sync\_with\_stdio 加速输入输出 - 码农场 (kineski)](https://www.hankcs.com/program/cpp/cin-tie-with-sync_with_stdio-acceleration-input-and-output.html)

[C++ 高速化 - Heavy Watal (japanski)](https://heavywatal.github.io/cxx/speed.html)

['Re: mmap/mlock performance versus read' - MARC](https://marc.info/?l=linux-kernel&m=95496636207616&w=2)
