---
title: Česte greške
---

Ova stranica navodi neke greške koje mnogi često čine na natjecanjima.

## Greške uzrokovane razlikama u okruženju

-   Upotreba oznake formata `%I64d` u `scanf` ili `printf` na Linuxu može uzrokovati pogrešan format učitavanja i ispisa.

## Greške koje uzrokuju CE

Ove su greške uglavnom leksičke, sintaktičke i semantičke; uzroci su im razmjerno jednostavni, a ispravljanje lako.

Primjeri:

-   Tipfeleri poput `int main()` napisanog kao `int mian()`.

-   Zaboravljena točka-zarez nakon `struct` ili `class`.

-   Preveliki nizovi, upotreba (na OJ-u) nedopuštenih funkcija (npr. višedretvenost) ili funkcija koja je deklarirana, ali nije definirana, uzrokuju greške pri povezivanju.

-   Nepodudaranje tipova argumenata funkcije.

    -   Primjer: pri pozivu funkcije `max` iz zaglavlja `<algorithm>` proslijeđen je jedan argument tipa `int` i jedan tipa `long long`.

        ```cpp
        // query je vlastita funkcija koja vraća long long
        printf("%lld\n", max(0, query(1, 1, n, l, r));

        //greška    nijedna instanca preopterećene funkcije "std::max" ne odgovara popisu argumenata
        ```

-   Preskakanje inicijalizacije nekih lokalnih varijabli pri upotrebi `goto` i `switch-case`.

## Greške koje ne uzrokuju CE, ali uzrokuju Warning

Program napisan s ovakvom greškom prolazi prevođenje, ali će najvjerojatnije dati pogrešan rezultat. Prevoditelj na ove greške upozorava pri prevođenju s opcijom `-W{warningtype}`.

-   Zamjena operatora pridruživanja `=` i operatora usporedbe `==`.

    -   Primjer:

        ```cpp
        std::srand(std::time(nullptr));
        int n = std::rand();
        if (n = 1)
          printf("Yes");
        else
          printf("No");

        // bez obzira na slučajnu vrijednost n, ispis je sigurno Yes
        // upozorenje    neispravan operator: pridruživanje konstante u Booleovu kontekstu. Razmislite o upotrebi „==”.
        ```

    -   Ako doista želite upotrijebiti `=` u naredbi u kojoj bi inače stajalo `==` (npr. `while (foo = bar)`), a ne želite dobiti Warning, možete upotrijebiti **dvostruke zagrade**: `while ((foo = bar))`.

-   Greške zbog prioriteta operatora.

    -   Primjer:

        ```cpp
        // pogrešno
        // std::cout << (1 << 1 + 1);
        // ispravno
        std::cout << ((1 << 1) + 1);

        // upozorenje    „<<”: provjerite prioritet operatora zbog moguće greške; zagradama razjasnite prioritet
        ```

-   Nepravilna upotreba modifikatora `static`.

-   Izostavljen operator adrese `&` pri učitavanju sa `scanf`.

-   Nepodudaranje tipa argumenta i oznake formata pri upotrebi `scanf` ili `printf`.

-   Istodobna upotreba bitovnih operacija i logičkog operatora `==` bez zagrada.
    -   Primjer: `(x >> j) & 3 == 2`

-   Prekoračenje literala tipa `int`.

    -   Primjer: `long long x = 0x7f7f7f7f7f7f7f7f`, `1<<62`.

-   Neinicijalizirane lokalne varijable.

    ???+ note "Što se događa s neinicijaliziranom varijablom"
        Izvornik: <https://loj.ac/d/3679>, autor @hly1204
        
        Na primjer, ako u C++-u deklariramo `int a;` bez inicijalizacije, ponekad mislimo da je `a` „slučajna” vrijednost (zapravo možda nije doista slučajna), a ponekad je smatramo nekom fiksnom vrijednošću, no u stvarnosti nije tako.
        
        U jednostavnom testnom kodu
        
        <https://wandbox.org/permlink/T2uiVe4n9Hg4EyWT>
        
        kod glasi:
        
        ```cpp
        #include <iostream>
        
        int main() {
          int a;
          std::cout << std::boolalpha << (a < 0 || a == 0 || a > 0);
          return 0;
        }
        ```
        
        Na nekim prevoditeljima i okruženjima, s uključenim optimizacijama, ispis je false.
        
        Ako vas zanima, pogledajte <https://www.ralfj.de/blog/2019/07/14/uninit.html>; iako je pokus napravljen u Rustu, bit je ista.

-   Lokalna varijabla istog imena kao globalna, zbog čega je globalna varijabla nehotice zasjenjena. (S opcijom `-Wshadow` ovakve se greške mogu otkriti.)

-   Greške u ispisu nakon preopterećenja operatora.
    -   Primjer:

        ```cpp
        // Namjera: prvi << je preopterećeni operator i označava ispis; drugi << je operator pomaka
        // i označava pomak broja 1 ulijevo za 1 mjesto. No zbog zaboravljenih zagrada prevoditelj i drugi <<
        // tumači kao operator ispisa, pa se rezultat ispisa razlikuje od očekivanog. Pogrešno: std::cout << 1 << 1; Ispravno:
        std::cout << (1 << 1);
        ```

## Greške koje ne uzrokuju ni CE ni Warning

Ove greške prevoditelj ne može otkriti; može ih se pronaći samo vlastitom provjerom.

### Greške koje dovode do WA

-   Nakon obrade jedne skupine podataka, a prije učitavanja sljedeće, nizovi nisu očišćeni.

-   Brzo učitavanje ne obrađuje negativne brojeve.

-   Nedovoljna širina upotrijebljenog tipa podataka, što dovodi do prekoračenja.
    -   Situacija koju opisuje izreka „tri godine OI-ja odu u vjetar ako ne staviš `long long`” (三年 OI 一场空，不开 `long long` 见祖宗). Natjecatelj gubi bodove jer na pravom mjestu nije upotrijebio `long long` (definirao cijeli broj kao `long long`), pa dobiva pogrešan odgovor.

-   Pri pohrani grafa vrhovi su numerirani od 0, a krajevi bridova u zadatku numerirani su od 1, pa je pri učitavanju zaboravljeno oduzeti 1.

-   Pogrešno ili obrnuto napisan znak veće/manje.

-   Nakon `ios::sync_with_stdio(false);` miješaju se `scanf/printf` i `std::cin/std::cout`, što dovodi do pomiješanog ulaza/izlaza.

    -   Primjer:

        ```cpp
        // Ovaj primjer pokazuje posljedice miješanja dvaju načina I/O-a nakon isključivanja sinkronizacije sa stdio
        // Preporučuje se izvršavanje korak po korak radi promatranja učinka
        #include <cstdio>
        #include <iostream>

        int main() {
          // Nakon isključivanja sinkronizacije cin/cout koriste vlastiti međuspremnik umjesto da izlaz sinkroniziraju
          // s međuspremnikom scanf/printf, čime se smanjuje vrijeme I/O-a
          std::ios::sync_with_stdio(false);
          // Kod cout, pri prelasku u novi red s '\n' sadržaj ostaje u međuspremniku i ne ispisuje se odmah
          std::cout << "a\n";
          // '\n' u printf prazni međuspremnik printf-a, pa se ispis pomiješa
          printf("b\n");
          std::cout << "c\n";
          // Međuspremnik cout-a ispisuje se tek na kraju programa
          return 0;
        }
        ```

-   Greške zbog razvijanja makroa bez zagrada.

    -   Primjer: ovaj makro ne vraća $4^2 = 16$, nego $2+2\times 2+2 = 8$.

        ```cpp
        #define square(x) x* x
        printf("%d", square(2 + 2));
        ```

-   Računske greške zbog neupotrebe `unsigned` pri hashiranju.
    -   Pomak udesno negativnog broja popunjava najviši bit jedinicom. Vidi: [Bitovni operatori](../lang/op.md#位操作符).

-   Nisu uklonjene ili zakomentirane naredbe za ispravljački ispis.

-   Suvišan `;`.

    -   Primjer:

        ```cpp
        /* clang-format off */
        while (1);
            printf("OI Wiki!\n");
        ```

-   Pogrešno postavljena vrijednost čuvara (sentinel). Na primjer, čvor `0` balansiranog stabla.

-   Pri inicijalizaciji varijabli pomoću `:` u konstruktoru klase ili strukture redoslijed deklaracije varijabli ne odgovara ovisnostima pri inicijalizaciji.

    -   Redoslijed inicijalizacije članova ovisi o redoslijedu njihove deklaracije u klasi, a ne o redoslijedu u listi inicijalizatora. Vidi: „Redoslijed inicijalizacije” u [Konstruktori i liste inicijalizatora članova](https://zh.cppreference.com/w/cpp/language/constructor)
    -   Primjer:

        ```cpp
        #include <iostream>

        class Foo {
         public:
          int a, b;

          // a će biti inicijaliziran prije b, a njegova vrijednost nije određena
          Foo(int x) : b(x), a(b + 1) {}
        };

        int main() {
          Foo bar(1, 2);
          std::cout << bar.a << ' ' << bar.b;
        }

        // Mogući ispis: -858993459 1
        ```

-   Pri spajanju skupova u union-findu nisu spojeni predstavnici (korijeni) dvaju elemenata.

    -   Primjer:

        ```cpp
        f[a] = b;              // pogrešno
        f[find(a)] = find(b);  // ispravno
        ```

-   `freopen` s načinom `a` (dopisivanje)
    -   Okruženje za ocjenjivanje CCF-a ne prazni izlaznu datoteku, pa s načinom `a` ocjenjivač učitava i ispis prethodnog natjecatelja, što uzrokuje WA

#### Različiti znakovi za novi red

???+ warning "Upozorenje"
    Na službenim natjecanjima nastoji se osigurati da okruženje u kojem natjecatelji rješavaju zadatke bude jednako okruženju završnog testiranja.
    
    Sadržaj ovog odjeljka odnosi se samo na situacije poput probnih natjecanja, a autorima zadataka preporučujemo da podaci po mogućnosti budu u skladu s [formatom podataka](problemsetting.md#format-podataka).

Različiti operacijski sustavi koriste različite znakove za označavanje novog reda; evo znakova novog reda nekoliko često korištenih sustava:

-   LF (označava se `\n`): `Unix` ili sustavi kompatibilni s `Unix`om

-   CR+LF (označava se `\r\n`): `Windows`

-   CR (označava se `\r`): `Mac OS` inačice 9 i starije

C/C++ za novi red koristi izlazni niz `\n`, zbog čega možemo pomisliti da se i novi red u ulazu sigurno označava s `\n`, pa učitamo samo jedan znak kao znak novog reda; tako ne učitamo ulaznu datoteku do kraja.

Rješenja:

-   Više puta pozvati `getchar()` dok se ne učita željeni znak.

-   Učitavati pomoću `cin`, **što može povećati konstantu programa**.

-   Pomoću `scanf("%s",str)` učitati string, a zatim uzeti `str[0]` kao učitani znak.

-   Pomoću `scanf(" %c",&c)` preskočiti sve bjeline.

### Greške koje dovode do nepredvidivog rezultata

Nedefinirano ponašanje dovodi do nepredvidivih rezultata, što može biti WA, RE i sl. Prevoditelj obično pretpostavlja da u programu nema nedefiniranog ponašanja, pa se kod može ponašati različito s uključenim O2 i bez njega.

-   Dijeljenje nulom (traženje inverza od 0)

    ???+ warning "Primjer"
        ```cpp
        cout << x / 0 << endl;
        ```

-   Prekoračenje granica niza (indeksa)

    Na primjer:

    -   Pogrešno postavljena početna vrijednost petlje dovodi do pristupa elementu s indeksom -1.

    -   Lista bridova neusmjerenog grafa nije dvostruko veća.

    -   Segment tree nema 4 puta više prostora.

    -   Pogrešno pročitan raspon podataka, jedna nula manje.

    -   Pogrešno procijenjena prostorna složenost algoritma.

    -   Pri pisanju segment treea `pushup` ili `pushdown` na listu.

        Ispravan postupak: ne prekoračujte granice, provjeravajte svoj kod tako da indeks `x` kojem pristupate bude unutar definiranih indeksa.

-   Funkcija s povratnom vrijednošću (osim main) izvršena do kraja bez ijedne naredbe return

    Čak i ako jedna grana vraća vrijednost, a druge ne, rezultat je nedefiniran.

    Opcijama prevođenja možete dodati `-Wall` i provjeriti upozorava li prevoditelj da funkcija nema return.

-   Pokušaj izmjene string literala

    ???+ warning "Primjer"
        ```cpp
        char *p = "OI-wiki";
        p[0] = 'o';
        p[1] = 'i';
        ```

    Ovakav pokušaj izmjene string literala dovodi do **nedefiniranog ponašanja**; treba upotrijebiti drugi, **prikladan** tip podataka, npr. `std::string` ili `char[]`.

-   Višestruko oslobađanje / nedopušteno dereferenciranje memorije

    Na primjer:

    -   Dereferenciranje neinicijaliziranog pokazivača.

    -   Memorija na koju pokazivač pokazuje već je oslobođena.

        Pri upotrebi `erase`, `delete` ili `free` pazite da istu adresu/objekt ne obradite više puta.

-   Pokušaj oslobađanja dijela bloka memorije dodijeljenog s `new []`

    Na primjer:

    ```cpp
    object *pool = new object[POOL_SIZE];

    object *pointer = pool + 10;

    // greška!
    delete pointer;
    ```

    Često se događa kad se nakon dodjele cijelog bloka memorije pomoću memory poola pojedini objekt dobiven iz poola pokuša osloboditi s `delete` ili `free()`.

-   Dereferenciranje nul-pokazivača / visećeg pokazivača

    Za nul-pokazivače: najprije provjerite je li pokazivač nul, npr. s `p == nullptr` ili `!p`.

    Za viseće pokazivače: pri oslobađanju pokazivač postavite na `nullptr` da biste to izbjegli.

-   Prekoračenje predznačenih brojeva

    Na primjer, imamo izraz `x+1 > x`.

    Normalan ispis trebao bi biti `true`, ali kad je `x` jednak `INT_MAX`, ispis je `false`; to se zove `signed integer overflow`.

    Možete upotrijebiti veći tip podataka (npr. `long long` ili `__int128`) ili provjeravati prekoračenje. Ako je zajamčeno da nema negativnih brojeva, možete upotrijebiti i nepredznačene cijele brojeve.

    Prekoračenje predznačenih cijelih brojeva može utjecati na optimizacije pri prevođenju; npr. kod:

    ```cpp
    int foo(int x) {
      if (x > x + 1) return 1;
      return 0;
    }
    ```

    prevoditelj može izravno optimizirati u:

    ```cpp
    int foo(int x) { return 0; }
    ```

    jer prevoditelj smije pretpostaviti da predznačeni cijeli brojevi nikad ne prekoračuju, pa `x > x + 1` nikad nije istinito.

-   Upotreba neinicijalizirane varijable

    ???+ warning "Primjer"
        ```cpp
        int foo(int a) {
          int t; /* nije inicijalizirano */
          if (/* upotreba */ t > 3) return a;
          return 0;
        }
        ```

### Greške koje dovode do RE

-   Nisu uklonjene operacije s datotekama (na nekim OJ-evima).

-   Pogrešna funkcija usporedbe pri sortiranju. `std::sort` zahtijeva da funkcija usporedbe bude strogi slabi uređaj: `a<a` je `false`; ako je `a<b` `true`, onda je `b<a` `false`; ako su `a<b` `true` i `b<c` `true`, onda je `a<c` `true`. Posebno pazite na drugu točku.
    Ako ti uvjeti nisu zadovoljeni, sortiranje vrlo vjerojatno završi s RE.
    Na primjer, pri pisanju sortiranja po parnosti za Moov algoritam ovako je pogrešno:

    ```cpp
    bool operator<(const int a, const int b) {
      if (block[a.l] == block[b.l])
        return (block[a.l] & 1) ^ (a.r < b.r);
      else
        return block[a.l] < block[b.l];
    }
    ```

    U gornjem kodu `(block[a.l]&1)^(a.r<b.r)` ne zadovoljava drugu točku gornjih uvjeta.
    Ovako je ispravno:

    ```cpp
    bool operator<(const int a, const int b) {
      if (block[a.l] == block[b.l])
        // pogrešno: ne zadovoljava uvjet strogog slabog uređaja
        // return (block[a.l] & 1) ^ (a.r < b.r);
        // ispravno
        return (block[a.l] & 1) ? (a.r < b.r) : (a.r > b.r);
      else
        return block[a.l] < block[b.l];
    }
    ```

-   Na Windowsu nedovoljan prostor stoga dovodi do prekoračenja stoga; Windows programu šalje signal SIGSEGV, program se prekida i vraća 3221225725 (tj. 0xC00000FD, NTSTATUS definiran kao `STATUS_STACK_OVERFLOW`).  
    Ako koristite prevoditelj gcc, pri prevođenju možete dodati `-Wl,--stack=SIZE` da biste zadali ograničenje veličine stoga, pri čemu je `SIZE` veličina stoga u bajtovima.

    Na Linuxu nedovoljan prostor stoga dovodi do prekoračenja stoga; Linux tada nasumično prepisuje `head_info` u stogu/hrpi, što u golemoj većini slučajeva dovodi do trenutačnog prekida programa s porukom poput `segmentation fault (core dumped)`.  
    U terminalu se pomoću `ulimit -s SIZE` može promijeniti ograničenje stoga za trenutačni terminal, pri čemu je `SIZE` veličina stoga u kilobajtima (KB).  
    **Napomena: ako ograničenje stoga postavite preveliko, beskonačna rekurzija može dovesti do prevelikog rekurzijskog stoga i time do rušenja sustava.**

### Greške koje dovode do TLE

-   Neprovjeren rubni uvjet u algoritmu podijeli pa vladaj dovodi do beskonačne rekurzije.

-   Beskonačna petlja.

    -   Isto ime varijabli petlji.

    -   Obrnut smjer petlje.

-   Pri BFS-u se ne označava je li stanje već posjećeno.

-   Pisanje min/max pomoću makroa

    Ova greška znatno povećava vrijeme izvođenja programa, a može čak izravno utjecati na vremensku složenost koda. Osobito je česta kad početnici pišu segment tree.

    Uobičajeni pogrešan način:

    ```cpp
    #define Min(x, y) ((x) < (y) ? (x) : (y))
    #define Max(x, y) ((x) > (y) ? (x) : (y))
    ```

    Ovako napisano nema problema s točnošću, ali ako se max izravno primijeni na povratne vrijednosti funkcija, npr. `a = Max(func1(), func2())`, a te se funkcije dugo izvršavaju, performanse programa znatno trpe, jer makro nakon razvijanja ima oblik `a = func1() > func2() ? func1() : func2()`, dakle funkcije se pozivaju tri puta – jednom više nego kod normalne funkcije max. Napomena: ako `func1()` svaki put vraća drugačiji odgovor, ovakav `max` daje i pogrešan rezultat, npr. kad je `func1()` oblika `return ++a;`, a `a` je globalna varijabla.

    Primjer: sljedeći se kod može srušiti na $\Theta(n)$ po upitu, što dovodi do TLE.

    ```cpp
    #define max(x, y) ((x) > (y) ? (x) : (y))

    int query(int t, int l, int r, int ql, int qr) {
      if (ql <= l && qr >= r) {
        ++ti[t];  // bilježimo broj posjeta čvoru radi lakšeg ispravljanja
        return vi[t];
      }

      int mid = (l + r) >> 1;
      if (mid >= qr) return query(lt(t), l, mid, ql, qr);
      if (mid < ql) return query(rt(t), mid + 1, r, ql, qr);
      return max(query(lt(t), l, mid, ql, qr), query(rt(t), mid + 1, r, ql, qr));
    }
    ```

-   Dodavanje znaka na string tipa `std::string` operatorom +

    Ova greška stvara privremenu varijablu tipa `string`, a nakon izmjene vrijednost se pridružuje izvornoj varijabli. Prevoditelj ovu grešku ne može optimizirati, pa kod velikih podataka može dovesti do degradacije vremenske složenosti.

    Uobičajen pogrešan način:

    ```cpp
    std::string a;
    char b = 'c';
    a = a + b;
    ```

    Pri izvršavanju ovog koda program najprije stvara privremenu varijablu tipa `string`, zatim u nju sprema vrijednost `a`, potom na kraj dodaje vrijednost `b` i na kraju je sprema u `a`.

    Iz [asemblerskog rezultata](https://godbolt.org/z/Eo9vn7or5) vidi se da `a = a + b` tri puta poziva funkcionalnost iz `std::__cxx11::basic_string`: `operator+`, `operator=` i stvaranje varijable.

    Ispravan način je:

    ```cpp
    std::string a;
    char b = 'c';
    a += b;
    ```

    [Ovaj način](https://godbolt.org/z/eGh33Grf3) izravno dodaje znak `b` na string `a`, pozivajući samo jednom `operator+=`. Detaljnija usporedba performansi: [Benchmark](https://quick-bench.com/q/JNDGl7HgOszNG-bo7AgVc42owv4).

-   Nisu uklonjene operacije s datotekama (na nekim OJ-evima).

-   Ponavljano izvršavanje funkcije složenosti različite od $O(1)$ u petlji `for/while`. Strogo govoreći, to može promijeniti vremensku složenost.

-   Pogrešna formula za sredinu ili pogrešan uvjet zaustavljanja pri binarnom pretraživanju.

### Greške koje dovode do MLE

-   Preveliki nizovi.

    ??? note "Detaljno o pokazateljima zauzeća memorije na Linuxu"
        > Ukratko: ako na ispitima CCF serije deklarirate iznimno velik globalni statički niz, budite posebno oprezni. Sav prostor koji program deklarira za nizove uračunava se u zauzeće memorije (za razliku od većine online platformi za ocjenjivanje, koje računaju samo stvarno iskorišteni dio), što u nekim slučajevima može dovesti čak do MLE na cijelom zadatku.
        
        -   O RSS-u i VSZ-u[^ref1][^ref2]
        
            1.  VSZ (Virtual Memory Size, veličina virtualne memorije)[^ref3]
        
                VSZ označava **veličinu virtualne memorije** procesa, tj. ukupnu veličinu virtualnog adresnog prostora kojem proces može pristupiti, obično prikazanu u KB.
        
                Virtualna memorija je logički pojam i obično je mnogo veća od stvarne upotrebe memorije.
        
                Na Linuxu naredbom `top` možete pogledati sastav zauzeća memorije nekog procesa; stupac `VIRT` predstavlja virtualnu memoriju koju zauzima.
        
                Virtualna memorija u pravilu uključuje i adresni prostor koji je proces dodijelio, ali ga stvarno ne koristi; ukratko, koliko je zatraženo, otprilike tolika je virtualna memorija.
        
                Posebno treba napomenuti da uobičajene online platforme za ocjenjivanje obično računaju samo zauzeće fizičke memorije. No **okruženje za ocjenjivanje CCF-a računa virtualnu memoriju**, što znači da ako deklarirate velik globalni statički niz, on zauzima mnogo prostora čak i ako koristite samo njegov mali dio.
            2.  RSS (Resident Set Size, veličina rezidentnog skupa)[^ref4]
        
                RSS označava **veličinu fizičke memorije** koju proces stvarno zauzima, tj. veličinu okvira stranica koje se nalaze u RAM-u, obično prikazanu u KB.
        
                Isto tako, pomoću `top` u stupcu `RES` možete vidjeti fizičku memoriju nekog procesa.
        
                RSS u pravilu obuhvaća samo dio koji je stvarno učitan u fizičku memoriju, tj. koliko se stvarno koristi, toliko iznosi.
        -   Analiza ponašanja zauzeća memorije
        
            Pretpostavimo da je deklariran sljedeći niz:
        
            ```cpp
            const int SIZE = 1e8;
            int arr[SIZE];  // zauzeće: 4 bajta * 100 milijuna = 400 MB
            ```
        
            To je statički niz, smješten u globalnom podatkovnom segmentu. Niz nije eksplicitno inicijaliziran, pa se obično smješta u segment BSS (ako je eksplicitno inicijaliziran (npr. sve nule ili druge vrijednosti), smješta se u segment DATA).
        
            -   Kad se niz uopće ne koristi (uz pretpostavku da ga prevoditelj ne optimizira)
        
                -   Fizička memorija: ako se nizu ne pristupa, mehanizam straničenja na zahtjev (Demand Paging) čini da stranice memorije još nisu učitane u fizičku memoriju. Fizička memorija se ne povećava ili se povećava tek neznatno (možda su učitane neke stranice metapodataka).
                -   Virtualna memorija: veličina niza uračunava se u virtualnu memoriju (povećanje za `400MB`), jer je virtualni adresni prostor cijelog niza već dodijeljen.
            -   Kad se koristi dio niza
        
                Pretpostavimo da se koristi samo nekoliko elemenata niza, npr.:
        
                ```cpp
                arr[0] = 1;
                arr[999999] = 2;
                ```
        
                -   Virtualna memorija: ne mijenja se, i dalje je `400MB`.
                -   Fizička memorija: pri svakom pristupu elementu niza odgovarajuća virtualna stranica učitava se u fizičku memoriju. Ako je veličina stranice sustava `4KB`, svaka stranica sadrži $4 \text{KB} ÷ 4 \text{B} = 1024$ elemenata tipa `int`. Dva pristupa nizu mogu učitati 2 stranice, tj. fizička memorija raste za oko $2 \times 4 \text{KB} = 8 \text{KB}$.
            -   Kad se koristi veći dio niza
        
                Pretpostavimo da se vrijednosti pridružuju prvim $50,000,000$ elemenata niza:
        
                ```cpp
                for (int i = 0; i < 50000000; ++i) {
                  arr[i] = i;
                }
                ```
        
                -   Virtualna memorija (VSZ): VSZ je i dalje `400MB`, ne mijenja se.
                -   Fizička memorija (RSS): riječ je o uzastopnom pristupu (pristupljenih $50,000,000$ elemenata susjedni su u memorijskim adresama), pa je broj stranica koje treba učitati $\left\lceil \dfrac{50,000,000}{1024} \right\rceil = 48,828$.
        
                    Uz veličinu stranice od `4KB` ukupno je to $48,828 \times 4 \text{KB} \approx 190 \text{MB}$, pa fizička memorija raste na oko `190MB`.
        
                    Napomena: ako se nizu pridružuju vrijednosti na slučajnim indeksima, zauzeće fizičke memorije znatno odstupa od procjene (jer se stranice učitavaju prema adresama, pa se pri slučajnom pridruživanju učitava velik broj stranica).
        
                Kratki sažetak: kako raste udio dijela kojem se pristupa, fizička memorija približava se virtualnoj (uz pretpostavku da nema oslobađanja stranica).
-   U STL spremnik umetnuto je previše elemenata.

    -   Često je riječ o beskonačnoj petlji u kojoj se umeću elementi u STL.

    -   Moguće je i da su vas srušili test podacima.

### Greške koje dovode do prevelike konstante

-   Modul nije definiran kao konstanta.

    -   Primjer:

        ```cpp
        // int mod = 998244353;      // pogrešno
        const int mod = 998244353;  // ispravno, prevoditelj ga može obraditi kao konstantu
        ```

-   Nepotrebna rekurzija (repna rekurzija ovdje nije uključena).

-   Pri pretvaranju rekurzije u iteraciju uvedeno je mnogo dodatnih operacija.

### Greške koje imaju učinak samo pri lokalnom izvođenju programa

-   Moguće greške pri radu s datotekama:

    -   Pri stress testiranju pokazivač na datoteku nije zatvoren s `fclose(fp)` prije ponovnog `fp = fopen()`. Zbog toga proces dobiva mnogo visećih pokazivača na datoteke.

    -   Imena datoteka u `freopen()` bez nastavka `.in`/`.out`.

-   Nakon upotrebe memorije na hrpi zaboravljeno je `delete` ili `free`.

## Reference i napomene

[^ref1]: [What is RSS and VSZ in Linux memory management - Stack Overflow](https://stackoverflow.com/questions/7880784/what-is-rss-and-vsz-in-linux-memory-management)

[^ref2]: [Need explanation on Resident Set Size/Virtual Size - Stack Overflow](https://unix.stackexchange.com/questions/35129/need-explanation-on-resident-set-size-virtual-size)

[^ref3]: [Virtualna memorija](https://en.wikipedia.org/wiki/Virtual_memory)

[^ref4]: [Veličina rezidentnog skupa](https://en.wikipedia.org/wiki/Resident_set_size)
