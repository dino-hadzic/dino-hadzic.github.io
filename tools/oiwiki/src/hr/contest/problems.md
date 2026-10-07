---
title: Pregled vrsta zadataka
---

Na algoritamskim natjecanjima postoje raznovrsne vrste zadataka.

## Klasični zadaci

**Klasični (tradicionalni) zadaci** trenutno su najčešća vrsta zadataka na algoritamskim natjecanjima.

Natjecatelj predaje izvorni kod, a sustav za ocjenjivanje koristi unaprijed pripremljene ulazne podatke i odgovarajuće izlazne podatke kao test-primjere[^note1]. Nakon što prevede natjecateljev izvorni kod[^note2], sustav natjecateljevu programu daje ulazne podatke i uspoređuje natjecateljev izlaz s unaprijed pripremljenim izlazom kako bi utvrdio je li program točan. Takav način ocjenjivanja zove se **ocjenjivanje crnom kutijom**[^note3].

Za svaki test-primjer obično se postavljaju i vremensko i memorijsko ograničenje.

Vremensko ograničenje odnosi se na ograničenje vremena izvođenja programa[^note4]. Vrijeme izvođenja natjecateljeva programa na jednom test-primjeru ne smije premašiti zadano vremensko ograničenje.

Memorijsko ograničenje odnosi se na ograničenje količine memorije koju program koristi. Najveća količina memorije koju natjecateljev program zauzme tijekom izvođenja ne smije premašiti zadano memorijsko ograničenje.

Nakon što program uredno završi, natjecateljev se izlaz uspoređuje s izlazom test-primjera. Ta usporedba obično se provodi kao usporedba cijelog teksta nakon uklanjanja završnih praznih redaka i razmaka na krajevima redaka. Za neke posebne zadatke usporedbu obavlja [Special Judge](../tools/special-judge.md).

Nakon tog postupka sustav za ocjenjivanje, ovisno o stanju izvođenja programa, daje različite **rezultate ocjenjivanja**[^note5]:

-   Accepted (AC): natjecateljev program je prihvaćen.
-   Compile Error (CE): natjecateljev program ne može se prevesti.
-   Wrong Answer (WA): natjecateljev program uredno je završio, ali se njegov izlaz ne podudara s izlazom test-primjera.
-   Presentation Error (PE): natjecateljev program uredno je završio, ali format izlaza ne odgovara zahtjevima[^note6].
-   Runtime Error (RE): natjecateljev program nije uredno završio (povratna vrijednost programa pri završetku nije nula).
-   Time Limit Exceeded (TLE): vrijeme izvođenja natjecateljeva programa premašilo je zadano vremensko ograničenje.
-   Memory Limit Exceeded (MLE): najveća količina memorije koju je natjecateljev program zauzeo premašila je zadano memorijsko ograničenje.
-   Output Limit Exceeded (OLE): količina podataka koju je natjecateljev program ispisao premašila je najveće dopušteno ograničenje.

Na ICPC natjecanjima vaš program mora dobiti AC na svim test-primjerima zadatka da bi se zadatak smatrao riješenim. Na OI natjecanjima dovoljno je dobiti AC na jednom test-primjeru da biste dobili bodove za taj test-primjer[^note7].

## Zadaci s predajom odgovora

**Zadaci s predajom odgovora** (output-only) zadaci su u kojima se izravno predaje odgovor. Takvi zadaci obično daju ulazne datoteke i traže predaju arhive, mape ili samih datoteka koje sadrže `XXX1.out`, `XXX2.out`, `XXX3.out`, …, `XXXn.out`.

Nakon predaje odgovora sustav za ocjenjivanje uspoređuje datoteke s odgovorima sa službenim odgovorima i, ovisno o kvaliteti natjecateljevih odgovora i stupnju dovršenosti zadatka, dodjeljuje određeni broj bodova.

Budući da se kod zadataka s predajom odgovora izvorni program ne izvodi, kod njih ne postoje vremenska ni memorijska ograničenja.

Takvi se zadaci obično rješavaju na dva načina:

-   ručno. Taj je način jednostavan i grub, ali kod većih podataka ne pomaže;
-   pisanjem programa koji proizvede datoteke s odgovorima.

## Interaktivni zadaci

**Interaktivni zadaci** zadaci su u kojima natjecateljev program mora komunicirati s programom za ocjenjivanje kako bi obavio zadatak. Čest je slučaj da natjecateljev program postavlja upite programu za ocjenjivanje i dobiva njegove odgovore. Program za ocjenjivanje može ograničavati natjecateljeve upite ili prilagođavati strategiju odgovaranja kako bi što više povećao broj upita, što zadacima donosi dodatnu raznolikost.

Detaljnije objašnjenje interaktivnih zadataka nalazi se na stranici [Interaktivni zadaci](./interaction.md).

Postoje dva glavna načina interakcije. Iako se tehnički znatno razlikuju, u pogledu algoritma koji se provjerava među njima nema stvarne razlike.

### STDIO interakcija

STDIO interakcija (interakcija preko standardnog ulaza/izlaza) način je interakcije na online platformama poput Codeforcesa i AtCodera, a standard je i na natjecanjima iz serije ICPC. Codeforces nudi sažetiji [opis (na engleskom)](https://codeforces.com/blog/entry/45307).

???+ note "Primjer zadatka [LOJ #559. LibreOJ Round #9, ZQC-ov labirint](https://loj.ac/problem/559)"
    Obratite pozornost na dodatak na kraju.
    
    Ovo je interaktivni zadatak.
    
    Nalazite se u mračnom labirintu od $n \times m$ polja i morate doći do njegova cilja kako biste izvršili izazov labirinta.
    
    Na početku se nalazite na početku labirinta, tj. na polju $(1,1)$, okrenuti udesno, a cilj je na polju $(n,m)$. Svaka dva polja labirinta međusobno su povezana i između njih postoji točno jedan put; udaljenost između dvaju susjednih polja (gore, dolje, lijevo, desno) jedna je jedinična duljina. Između dvaju susjednih polja može biti zid; debljina zida zanemariva je u odnosu na polje. Rubovi labirinta su zidovi, a svaki je zid povezan s rubom. Labirint je potpuno mračan, što znači da ne možete dobiti nikakvu informaciju osim $(n,m)$.
    
    Kako se u mraku ne biste izgubili, pri svakom koraku možete krenuti samo s trenutnog polja uz lijevi ili desni zid, držeći se lijevom ili desnom rukom za zid, i to tako da ruka na zidu prijeđe točno jednu jediničnu duljinu. Pazite: ako lijevi ili desni zid ne postoji, u tom se smjeru ne možete kretati.
    
    Ako predugo ostanete u mraku, uplašit ćete se, pa iz labirinta morate izaći što prije. Ako ne izađete iz labirinta unutar zadanog broja koraka, izazov nije uspio.

Kod takvih zadataka natjecatelj upite kao i obično piše na standardni izlaz, **isprazni izlazni međuspremnik** i zatim čita rezultat sa standardnog ulaza. Tek kad natjecateljev program isprazni izlazni međuspremnik, program za ocjenjivanje povezan s njim cijevima (zvan interaktor) može odmah primiti te podatke. U C-u/C++-u to rade `fflush(stdout)` i `std::cout << std::flush` (`std::cout << std::endl` pri prelasku u novi red također automatski prazni međuspremnik, ali `std::cout << '\n'` ne); u Pascalu je to `flush(output)`.

### Interakcija preko gradera

Interakcija preko gradera česta je na međunarodnim OI natjecanjima poput IOI-ja i APIO-a (osobito na natjecanjima koja koriste platformu CMS).

???+ note "Primjer zadatka [UOJ #206. APIO2016 Gap](https://uoj.ac/problem/206)"
    Zadano je $N$ strogo rastućih nenegativnih cijelih brojeva $a_1,a_2,\cdots,a_N (0\leq a_1<a2<\cdots<a_N\leq 10^{18})$. Trebate pronaći najveću vrijednost među $a_{i+1}−a_i (0\leq i\leq N−1)$.
    
    Vaš program ne može izravno učitati taj niz brojeva, ali informacije o nizu možete dobiti pozivanjem zadane funkcije. Pojedinosti o funkciji za upite potražite u odjeljku o detaljima implementacije u nastavku, ovisno o jeziku koji koristite.
    
    Trebate implementirati funkciju koja vraća najveću vrijednost među $a_{i+1}−a_i (0\leq i\leq N−1)$.

Kod takvih zadataka natjecatelj piše samo određenu funkciju koja obavlja neki zadatak, a interakciju provodi pozivanjem nekoliko zadanih pomoćnih funkcija. Radi lakšeg lokalnog testiranja uz zadatak se dijele datoteka zaglavlja i referentni program za ocjenjivanje `grader.cpp` (za Pascal biblioteka `graderlib`); natjecatelj svoj program prevodi zajedno s `grader.cpp` kako bi dobio izvršnu datoteku.

```sh
g++ grader.cpp my_solution.cpp -o my_solution -Wall -O2
./my_solution   # pokretanje programa
```

Prevedeni program ponaša se slično programu za klasični zadatak. Otvara unaprijed određene datoteke, čita podatke u unaprijed određenom formatu, poziva natjecateljevu funkciju te ispisuje rezultat i neke informacije (npr. broj upita, točnost odgovora) na standardni izlaz.

Pri stvarnom ocjenjivanju natjecateljev se program prevodi s drugačijim `grader.cpp`. Taj `grader.cpp` na sličan način poziva natjecateljevu funkciju i bilježi bodove. U pravilu su u toj inačici `grader.cpp` svi globalni simboli označeni kao `static`, pa ga se ne može zaobići sukobom imena, ali svaki pokušaj zaobilaženja ograničenja gradera kažnjava se diskvalifikacijom (disqualification).

### Razlike

Očita prednost STDIO interakcije jest da podržava bilo koji programski jezik, ali vrijeme potrošeno na ulaz i izlaz lako postaje usko grlo pri sastavljanju zadatka, pa se ponekad ne mogu razlikovati programi različite vremenske učinkovitosti. Interakcija preko gradera upravo je suprotna: budući da je trošak poziva funkcije malen, često se može dopustiti i $10^6$ upita, ali joj je slabost ograničenje na određene jezike.

Ako sami sastavljate zadatke ili organizirate natjecanje, oba pristupa treba pažljivo odvagnuti i usporediti.

## Komunikacijski zadaci

**Komunikacijski zadaci** zadaci su u kojima dva natjecateljeva programa moraju komunicirati i zajedno obaviti neki zadatak. Prvi program prima ulaz problema i proizvodi neki izlaz; ulaz drugog programa povezan je s izlazom prvoga (ponekad se predaje nepromijenjen kao parametar, a ponekad ga obrađuje sustav za ocjenjivanje) i on mora proizvesti rješenje problema.

Primjeri komunikacijskih zadataka: [UOJ #178. Novogodišnja čestitka](https://uoj.ac/problem/178), [#454. UER #8, Grudanje](https://uoj.ac/problem/454) i drugi.

Načini lokalnog testiranja razlikuju se ovisno o postavkama zadatka; uobičajeni su oblici:

-   ručni unos;
-   pisanje pomoćnog programa koji izlaz prvog programa pretvara u ulaz drugog;
-   povezivanje standardnih ulaza/izlaza dvaju programa dvosmjernim cijevima.

Budući da platforme za ocjenjivanje slabo podržavaju komunikacijske zadatke, oni su zasad česti samo na natjecanjima serije IOI i na nekolicini online platformi poput UOJ-a. To je i dalje područje koje tek treba istražiti.

## Zadaci dopunjavanja funkcije

**Zadaci dopunjavanja funkcije** zadaci su u kojima natjecatelj mora dopuniti program. Mogu se shvatiti kao interaktivni zadatak u kojem je natjecateljev kod zadan, a traži se pisanje pomoćnih funkcija.

Obično se pojavljuju u sljedećim oblicima:

-   zadan je program i rečeno je gdje će se ugraditi blok koda koji treba dopuniti;
-   program nije zadan, nego se ulazni podaci predaju kao parametri funkcije koju treba predati.

Takvi su zadaci česti na platformama [LeetCode](https://leetcode.com/) i [PTA - Pintia](https://pintia.cn/problem-sets).

## Ostale vrste

???+ note "Primjer zadatka [Quine](https://loj.ac/problem/4)"
    Napišite program koji ispisuje vlastiti izvorni kod.
    
    Kod mora sadržavati barem deset vidljivih znakova.

Zadatak je vrlo klasičan, ali ga je na velikoj većini online sudaca teško ostvariti.

??? note "Referentni kod"
    **Napomena**: izvorni kod ne uključuje prvi redak u nastavku (tj. `// clang-format off`).
    
    ```cpp
    // clang-format off
    #include<cstdio>
    
    char *s={"#include<cstdio>%cchar *s={%c%s%c};%cint main(){printf(s,10,34,s,34,10);return 0;}"};
    
    int main(){printf(s,10,34,s,34,10);return 0;}
    ```

## Literatura i bilješke

[^note1]: Zbog tehničkih i resursnih ograničenja test-primjeri jednog zadatka u većini slučajeva ne mogu pokriti sve podatke koji zadovoljavaju zadana ograničenja.

[^note2]: Za interpretirane jezike poput Pythona program izravno izvodi interpreter.

[^note3]: Zapravo je implementacija sustava za ocjenjivanje mnogo složenija; ovdje je postupak ocjenjivanja opisan samo u grubim crtama.

[^note4]: Točnije, obično je riječ o korisničkom vremenu (user time) programa.

[^note5]: Ovi rezultati ocjenjivanja većinom vrijede i za druge vrste zadataka.

[^note6]: Većina sustava za ocjenjivanje status PE svrstava pod WA.

[^note7]: Neki test-primjeri mogu nositi djelomične bodove: ako natjecatelj riješi dio zadatka na test-primjeru ili je njegov izlaz točan, ali nije dovoljno dobar, može dobiti određeni udio bodova.
