---
title: Prosti brojevi
---

Definicije prostih i složenih brojeva vidi u [Osnovama teorije brojeva](./basic.md).

Funkcija prebrojavanja prostih brojeva: broj prostih brojeva manjih ili jednakih $x$ označava se s $\pi(x)$. Kako $x$ raste, vrijedi sljedeća aproksimacija: $\pi(x) \sim \dfrac{x}{\ln(x)}$.

## Testiranje prostosti

**Test prostosti** (primality test) služi za utvrđivanje je li zadani prirodni broj prost.

Postoje dvije vrste testova prostosti:

1.  Deterministički testovi: sa sigurnošću utvrđuju je li broj prost. Uobičajeni su primjeri probno dijeljenje, Lucas–Lehmerov test i dokaz prostosti eliptičkim krivuljama.
2.  Probabilistički testovi: obično su znatno brži od determinističkih, ali mogu (iako s vrlo malom vjerojatnošću) pogrešno proglasiti [složen broj](./basic.md#素数与合数) prostim (obrnuto se ne događa). Zato se brojevi koji prođu probabilistički test prostosti nazivaju **vjerojatno prostima** sve dok se njihova prostost ne dokaže deterministički. Brojevi koji prođu test, a zapravo su složeni, nazivaju se **pseudoprostima**. Postoji mnogo posebnih vrsta pseudoprostih brojeva; najčešći su Fermatovi pseudoprosti brojevi – složeni brojevi koji zadovoljavaju mali Fermatov teorem. Uobičajen primjer probabilističkog testa je Miller–Rabinov test.

### Probno dijeljenje

Grubom silom, naravno, možemo redom isprobati svaki broj od najmanjeg prema većima i provjeriti dijeli li zadani broj.

???+ example "Referentna implementacija"
    === "C++"
        ```cpp
        bool isPrime(int a) {
          if (a < 2) return false;
          for (int i = 2; i < a; ++i)
            if (a % i == 0) return false;
          return true;
        }
        ```
    
    === "Python"
        ```python
        def isPrime(a):
            if a < 2:
                return False
            for i in range(2, a):
                if a % i == 0:
                    return False
            return True
        ```

To je sasvim pouzdano, ali je li doista potrebno provjeriti svaki broj?

Lako se uočava sljedeća činjenica: ako je $x$ djelitelj od $a$, onda je i $\frac{a}{x}$ djelitelj od $a$.

Taj nam zaključak govori da je za svaki par $(x, \frac{a}{x} )$ dovoljno provjeriti samo jedan od njih. Radi jednostavnosti promatramo samo manji broj svakog para. Nije teško uočiti da svi ti manji brojevi leže u intervalu $[1, \sqrt{a}]$.

Budući da je $1$ sigurno djelitelj, njega ne provjeravamo.

???+ example "Referentna implementacija"
    === "C++"
        ```cpp
        bool isPrime(int a) {
          if (a < 2) return 0;
          for (int i = 2; (long long)i * i <= a; ++i)  // sprječava prekoračenje
            if (a % i == 0) return 0;
          return 1;
        }
        ```
    
    === "Python"
        ```python
        def isPrime(a):
            if a < 2:
                return False
            for i in range(2, int(sqrt(a)) + 1):
                if a % i == 0:
                    return False
            return True
        ```

### Fermatov test prostosti

**Fermatov test prostosti** najjednostavniji je probabilistički test prostosti.

Iz [malog Fermatova teorema](./fermat.md#费马小定理) možemo izvesti ideju za provjeru prostosti:

Osnovna je zamisao uzastopno birati baze $a$ iz $[2, n-1]$ i provjeravati vrijedi li svaki put $a^{n-1} \equiv 1 \pmod n$.

???+ example "Referentna implementacija"
    === "C++"
        ```cpp
        bool fermat(int n) {
          if (n < 3) return n == 2;
          // test_time je broj testova; preporučuje se cijeli broj ne manji od 8
          // radi točnosti, ali ni prevelik, jer bi to narušilo učinkovitost
          for (int i = 1; i <= test_time; ++i) {
            int a = rand() % (n - 2) + 2;
            if (quickPow(a, n - 1, n) != 1) return false;
          }
          return true;
        }
        ```
    
    === "Python"
        ```python
        def fermat(n):
            if n < 3:
                return n == 2
            # test_time je broj testova; preporučuje se cijeli broj ne manji od 8
            # radi točnosti, ali ni prevelik, jer bi to narušilo učinkovitost
            for i in range(1, test_time + 1):
                a = random.randint(0, 32767) % (n - 2) + 2
                if quickPow(a, n - 1, n) != 1:
                    return False
            return True
        ```

Ako je $a^{n-1} \equiv 1 \pmod n$, a $n$ nije prost, $n$ se naziva **Fermatov pseudoprost broj** za bazu $a$. U praksi opažamo da je, ako vrijedi $a^{n-1} \equiv 1 \pmod n$, broj $n$ obično prost. No postoje protuprimjeri: za $n = 341$ i $a = 2$ vrijedi $2^{340}\equiv 1 {\pmod {341}}$, ali $341 = 11 \cdot 31$ je složen. Zapravo, za svaku fiksnu bazu $a$ takvih protuprimjera ima beskonačno mnogo[^inf-fermat-pp].

Budući da Fermatov test prostosti s jednom bazom ne jamči točnost, prirodna je ideja provjeriti više baza. Međutim, čak i ako provjerimo sve moguće baze $a$ relativno proste s $n$, i dalje ne možemo jamčiti da je $n$ prost. Drugim riječima, obrat malog Fermatova teorema ne vrijedi: čak i ako za sve $a\perp n$ vrijedi $a^{n-1}\equiv 1\pmod n$, $n$ ne mora biti prost. Takvi se brojevi nazivaju [Carmichaelovi brojevi](./primitive-root.md#carmichael-数). I njih ima beskonačno mnogo. To nas prisiljava da potražimo stroži test prostosti.

### Miller–Rabinov test prostosti

**Miller–Rabinov test prostosti** (Miller–Rabin primality test) bolja je metoda provjere prostosti. Dobili su ga Miller i Rabin poboljšanjem Fermatova testa prostosti. Kao i ostali probabilistički testovi prostosti, i on može otkriti samo vjerojatno proste brojeve. Da bismo bili sigurni da je broj prost, potreban je znatno sporiji deterministički algoritam. Ipak, do sada nije pronađen nijedan složen broj koji bi prošao Miller–Rabinov test ili druge napredne probabilističke testove, pa ga možemo bezbrižno koristiti.

Ne uzimajući u obzir složenost množenja, vremenska složenost $k$ krugova testa za broj $n$ iznosi $O(k \log n)$. Miller–Rabinov test prostosti često se koristi za brojeve velike preciznosti; tada je vremenska složenost $O(k \log^3n)$, a tehnikama poput FFT-a može se poboljšati do [$O(k \log^2n \log \log n \log \log \log n)$](https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test#Complexity).

Kako bi se riješio problem Carmichaelovih brojeva, Miller–Rabinov test prostosti dodatno koristi sljedeće svojstvo prostih brojeva:

???+ note "Teorem o kvadratnoj provjeri"
    Ako je $p$ neparan prost broj, rješenja jednadžbe $x^2 \equiv 1 \pmod p$ su $x \equiv 1 \pmod p$ ili $x \equiv p - 1 \pmod p$.

??? note "Dokaz"
    Lako se provjerava da za neparan prost $p$ i $x\equiv 1\pmod p$ i $x\equiv p-1\pmod p$ zadovoljavaju gornju jednadžbu. Po [Lagrangeovu teoremu](./congruence-equation.md#素数模同余方程) to su sva rješenja te jednadžbe.

Kombinirajući mali Fermatov teorem i teorem o kvadratnoj provjeri dobivamo Miller–Rabinov test prostosti:

1.  Eksponent $n-1$ u $a^{n-1} \equiv 1 \pmod n$ rastavimo kao $n-1=u \times 2^t$, gdje je $u$ neparan;
2.  U svakom krugu testa za slučajno odabrani $a$ najprije izračunamo $v = a^{u} \bmod n$, a zatim tu vrijednost najviše $t$ puta kvadriramo;
3.  Ako tijekom tog postupka pronađemo netrivijalni kvadratni korijen od $1$ (tj. korijen različit od $\pm 1$), možemo zaključiti da broj nije prost;
4.  Inače još primijenimo Fermatov test prostosti.

Još nekoliko sitnih detalja implementacije:

-   Ako u nekom krugu testa u nekom trenutku vrijedi $a^{u \times 2^s} \equiv n-1 \pmod n$, sva daljnja kvadriranja dat će $1$, pa taj krug testa možemo odmah proglasiti uspješnim.
-   Ako pronađemo netrivijalni kvadratni korijen, tj. $a^{u \times 2^s} \not\equiv n-1 \text{ or } 1 \pmod n$, a $a^{u \times 2^{s+1}} \equiv 1 \pmod n$, sva daljnja kvadriranja dat će $1$. Možemo odmah vratiti `false`, a možemo i pričekati kraj $t$ kvadriranja i tek onda vratiti `false`.

Tako dobivamo ispravniji Miller–Rabin (autor: fjzzq2002):

???+ example "Referentna implementacija"
    === "C++"
        ```cpp
        bool millerRabin(int n) {
          if (n < 3 || n % 2 == 0) return n == 2;
          if (n % 3 == 0) return n == 3;
          int u = n - 1, t = 0;
          while (u % 2 == 0) u /= 2, ++t;
          // test_time je broj testova; preporučuje se cijeli broj ne manji od 8
          // radi točnosti, ali ni prevelik, jer bi to narušilo učinkovitost
          for (int i = 0; i < test_time; ++i) {
            // 0, 1, n-1 odmah prolaze test, a se bira iz raspona [2, n-2]
            int a = rand() % (n - 3) + 2, v = quickPow(a, u, n);
            if (v == 1) continue;
            int s;
            for (s = 0; s < t; ++s) {
              if (v == n - 1) break;  // dobiven trivijalni kvadratni korijen n-1, ovaj krug testa prolazi
              v = (long long)v * v % n;
            }
            // ako je pronađen netrivijalni kvadratni korijen, petlja se ne može prekinuti ranije pa se dođe do s == t
            // ako Fermatov test prostosti ne prolazi, v nikad nije jednak -1 prije nego što se dođe do s == t
            if (s == t) return 0;
          }
          return 1;
        }
        ```
    
    === "Python"
        ```python
        def millerRabin(n):
            if n < 3 or n % 2 == 0:
                return n == 2
            if n % 3 == 0:
                return n == 3
            u, t = n - 1, 0
            while u % 2 == 0:
                u = u // 2
                t = t + 1
            # test_time je broj testova; preporučuje se cijeli broj ne manji od 8
            # radi točnosti, ali ni prevelik, jer bi to narušilo učinkovitost
            for i in range(test_time):
                # 0, 1, n-1 odmah prolaze test, a se bira iz raspona [2, n-2]
                a = random.randint(2, n - 2)
                v = pow(a, u, n)
                if v == 1:
                    continue
                s = 0
                while s < t:
                    if v == n - 1:
                        break
                    v = v * v % n
                    s = s + 1
                # ako je pronađen netrivijalni kvadratni korijen, petlja se ne može prekinuti ranije pa se dođe do s == t
                # ako Fermatov test prostosti ne prolazi, v nikad nije jednak -1 prije nego što se dođe do s == t
                if s == t:
                    return False
            return True
        ```

Može se dokazati[^millerrabinproof] da je vjerojatnost da neparan složen broj $n > 9$ prođe Miller–Rabinov test prostosti za jednu slučajno odabranu bazu $a$ najviše jedna četvrtina. Stoga nakon slučajnog odabira $k$ baza vjerojatnost da složen broj pogrešno proglasimo prostim ne prelazi $1/4^k$.

??? note "Dokaz"
    Neka je $n-1=u2^t$, gdje je $u$ neparan, a $t$ pozitivan cijeli broj. Tada cijeli broj $n$ prolazi Miller–Rabinov test prostosti s bazom $a$ upravo onda kada
    
    $$
    a^u\equiv 1{\textstyle\pmod n},\text{ or }a^{u2^i}\equiv -1{\textstyle\pmod n}\text{ for some }0\le i < t.
    $$
    
    Označimo skup takvih $a$ (odnosno njihovih klasa kongruencije) sa $S$; treba pokazati da je
    
    $$
    |S| \le \dfrac14\varphi(n).
    $$
    
    Ovdje je $\varphi(n)$ [Eulerova funkcija](./euler-totient.md). Dokaz ima tri koraka.
    
    **Prvi korak**: neka je $\ell$ najveći pozitivan cijeli broj takav da $2^\ell \mid p-1$ vrijedi za sve proste faktore $p$ broja $n$. Tada se može pokazati da je
    
    $$
    S\subseteq S' = \{a\bmod n:a^{u2^{\ell-1}}\equiv\pm 1{\textstyle\pmod n}\}.
    $$
    
    Za element $a$ skupa $S$ postoje samo dvije mogućnosti. Ako je $a^u\equiv 1\pmod n$, očito vrijedi i $a^{u2^{\ell-1}}\equiv 1\pmod n$, tj. $a\in S'$. Ako za neki $0\le i < t$ vrijedi $a^{u2^i}\equiv -1\pmod n$, onda za svaki prosti faktor $p\mid n$ vrijedi $a^{u2^i}\equiv-1\pmod p$. Neka je $\delta_p(a)$ [red](./primitive-root.md#阶) elementa $a$ modulo $p$; tada očito $\delta_p(a)\mid u2^{i+1}$, ali $\delta_p(a)\nmid u2^{i}$, što znači da je u rastavu $\delta_p(a)$ na proste faktore eksponent od $2$ točno $i+1$, pa $2^{i+1}\mid\delta_p(a)$. Po malom Fermatovu teoremu $\delta_p(a)\mid p-1$, pa je $2^{i+1}\mid p-1$. To vrijedi za sve proste faktore $p$ broja $n$. Stoga je $i+1\le\ell$. Odatle $a^{u2^{\ell-1}} = (a^{u2^i})^{2^{\ell-1-i}} \equiv \pm 1 \pmod n$, pa je opet $a\in S'$. Objedinjujući obje mogućnosti dobivamo $S\subseteq S'$.
    
    **Drugi korak**: izračunajmo $|S'|$.
    
    Neka je rastav broja $n$ na proste faktore $n = p_1^{e_1}p_2^{e_2}\cdots p_k^{e_k}$. Po [kineskom teoremu o ostatcima](./crt.md) uvjet $a^{u2^{\ell - 1}}\equiv 1\pmod n$ ekvivalentan je tome da $a^{u2^{\ell - 1}}\equiv 1\pmod{p_i^{e_i}}$ vrijedi za sve $p_i^{e_i}$. Budući da [primitivni korijen](./primitive-root.md#原根) modulo potencija neparnog prostog broja $p_i^{e_i}$ uvijek postoji, [broj rješenja](./residue.md#性质) kongruencije $a^{u2^{\ell - 1}}\equiv 1\pmod{p_i^{e_i}}$ jednak je
    
    $$
    \gcd(u2^{\ell-1},p_i^{e_i-1}(p_i-1)) = \gcd(u2^{\ell-1},p_i-1) = 2^{\ell-1}\gcd(u,p_i-1).
    $$
    
    Prva jednakost vrijedi jer je $u$ djelitelj od $n-1$ pa ne može biti višekratnik od $p_i$; druga jednakost vrijedi zbog načina na koji je odabran $\ell$. Stoga je, po kineskom teoremu o ostatcima, broj rješenja kongruencije $a^{u2^{\ell-1}}\equiv 1\pmod n$ jednak
    
    $$
    \prod_{p\mid n}2^{\ell-1}\gcd(u,p-1).
    $$
    
    Slično, uvjet $a^{u2^{\ell - 1}}\equiv -1\pmod n$ ekvivalentan je tome da $a^{u2^{\ell - 1}}\equiv -1\pmod{p_i^{e_i}}$ vrijedi za sve $p_i^{e_i}$. Za svaki faktor $p_i^{e_i}$ uvjet $a^{u2^{\ell - 1}}\equiv -1\pmod{p_i^{e_i}}$ ekvivalentan je tome da vrijedi $a^{u2^{\ell - 1}}\not\equiv 1\pmod{p_i^{e_i}}$ i $a^{u2^{\ell}}\equiv 1\pmod{p_i^{e_i}}$. Slično kao gore, broj rješenja kongruencije $a^{u2^{\ell}}\equiv 1\pmod{p_i^{e_i}}$ jednak je $2^{\ell}\gcd(u,p_i-1)$, pa je broj rješenja kongruencije $a^{u2^{\ell - 1}}\equiv -1\pmod{p_i^{e_i}}$ također jednak
    
    $$
    2^{\ell}\gcd(u,p_i-1) - 2^{\ell-1}\gcd(u,p_i-1) = 2^{\ell-1}\gcd(u,p_i-1).
    $$
    
    Ponovnom primjenom kineskog teorema o ostatcima dobivamo da je broj rješenja kongruencije $a^{u2^{\ell - 1}}\equiv -1\pmod n$ jednak
    
    $$
    \prod_{p\mid n}2^{\ell-1}\gcd(u,p-1).
    $$
    
    Objedinjujući oba slučaja dobivamo
    
    $$
    |S'| = 2\prod_{p\mid n}2^{\ell-1}\gcd(u,p-1).
    $$
    
    **Treći korak**: dokažimo da je $|S'|\le\varphi(n)/4$.
    
    Iz izraza za Eulerovu funkciju $\varphi(n)=\prod_ip_i^{e_i-1}(p_i-1)$ slijedi
    
    $$
    \dfrac{\varphi(n)}{|S'|} = \dfrac{1}{2}\prod_ip_i^{e_i-1}\dfrac{p_i-1}{2^{\ell-1}\gcd(u,p_i-1)}.
    $$
    
    Za svaki $i$ odgovarajući faktor $p_i^{e_i-1}\dfrac{p_i-1}{2^{\ell-1}\gcd(u,p_i-1)}$ paran je broj, pa je $\varphi(n)/|S'|$ cijeli broj. Pretpostavimo da $|S'|\le\varphi(n)/4$ ne vrijedi. Tada je nužno $\varphi(n)/|S'|=1,2,3$, tj.
    
    $$
    \prod_ip_i^{e_i-1}\dfrac{p_i-1}{2^{\ell-1}\gcd(u,p_i-1)} = 2,4,6.
    $$
    
    Budući da je svaki faktor u produktu paran, produkt ili ima samo jedan faktor i taj je jednak $2,4,6$, ili ima točno dva faktora i oba su jednaka $2$.
    
    Razmotrimo najprije slučaj s dva faktora. Tada nijedan od tih dvaju faktora nema neparan prosti faktor, pa je $p_i^{e_i-1}=1$, tj. $n$ nema kvadratnih faktora. Bez smanjenja općenitosti neka je $n=p_1p_2$, gdje su $p_1<p_2$ prosti brojevi. Oba su faktora jednaka $2$, pa uvijek vrijedi $p_i-1=2^{\ell}\gcd(u,p_i-1)$. Stoga je $p_i=1+2^\ell m_i$, gdje je $m_i$ neparan i $m_i\mid u$. Uzmemo li $p_1p_2=n=1+u2^t$ modulo $m_1$, dobivamo $p_1p_2\equiv 1\pmod{m_1}$, pa je $p_2\equiv 1\pmod{m_1}$, što znači da $m_1\mid m_2$. Vrijedi i obrnuto. Dakle $m_1=m_2$, tj. $p_1=p_2$. To je u suprotnosti s $p_1<p_2$. Ovaj slučaj nije moguć.
    
    Naposljetku razmotrimo slučaj s jednim faktorom, tj. složen broj $n=p^e$ uz $e>1$. Tada nužno $p^{e-1}\mid 2,4,6$. Jedina je mogućnost $p=3,e=2$, tj. $n=9$, što je u suprotnosti s pretpostavkom tvrdnje. Ni ovaj slučaj nije moguć.
    
    Objedinjujući sve slučajeve zaključujemo da vrijedi $|S'|\le\varphi(n)/4$.
    
    Iz gornja tri koraka slijedi da $|S|\le |S'|\le \varphi(n)/4$ vrijedi za sve neparne složene brojeve $n>9$.

Osim toga, ako pretpostavimo da vrijedi [generalizirana Riemannova hipoteza](https://en.wikipedia.org/wiki/Generalized_Riemann_hypothesis) (generalized Riemann hypothesis, GRH), tada je za broj $n$ dovoljno testirati sve cijele brojeve iz $[2, \min\{n-2, \lfloor 2\ln^2 n \rfloor\}]$ da bi se prostost broja $n$ **sa sigurnošću** utvrdila.[^deterministic-proof]

U okvirima OI-ja prostost se obično provjerava za brojeve iz raspona $[1, 2^{64})$. Za brojeve iz $[1, 2^{32})$ dovoljno je kao baze Miller–Rabinova testa prostosti uzeti tri broja $\{2, 7, 61\}$ da bi se prostost utvrdila sa sigurnošću; za brojeve iz $[1, 2^{64})$ dovoljno je kao baze Miller–Rabinova testa prostosti uzeti sedam brojeva $\{2, 325, 9375, 28178, 450775, 9780504, 1795265022\}$.[^witnesses]

Za provjeru prostih brojeva iz $[1, 2^{64})$ može se uzeti i $\{2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37\}$ (tj. prvih $12$ prostih brojeva).

Ako brojeve $a$ iz gornjih nizova koristimo kao baze za provjeru prostosti broja $n$, treba paziti na sljedeće:

-   treba proći kroz sve brojeve, ne samo one manje od $n$;
-   $a$ zamijenimo s $a \bmod n$;
-   ako je $a \equiv 0 \pmod n$ ili $a \equiv \pm 1 \pmod n$, taj krug testa odmah prolazi.

## Antiprosti brojevi

Kao što samo ime kaže, prost broj ima točno dva djelitelja, a antiprost broj ima najviše djelitelja (a pri jednakom broju djelitelja najmanju vrijednost); antiprostost se dakle definira u odnosu na neki skup.

Intuitivna definicija antiprostog broja glasi: u skupu pozitivnih cijelih brojeva antiprost je onaj broj koji ima najviše djelitelja i najmanju vrijednost.

???+ abstract "Antiprost broj"
    Ako za pozitivan cijeli broj $n$ svaki pozitivan cijeli broj manji od $n$ ima manje djelitelja od $n$, onda $n$ nazivamo **antiprostim** (anti-prime, poznat i kao visoko složen broj, highly composite number).

???+ warning "Napomena"
    Ne treba ga miješati s pojmom [emirp](https://en.wikipedia.org/wiki/Emirp), koji označava prost broj čije znamenke pročitane unatrag daju drugi prost broj (npr. 149 i 941 su emirpi, a 101 nije).

### Postupak

Kako, dakle, naći antiproste brojeve?

Najprije, budući da nas zanima broj djelitelja, prvo što treba napraviti jest rastav na proste faktore. Rastavimo li $n$ u oblik $n=p_{1}^{k_{1}}p_{2}^{k_{2}} \cdots p_{m}^{k_{m}}$, gdje su $p$ prosti brojevi, a $k$ njihovi eksponenti, ukupan broj djelitelja jednak je $(k_1+1) \times (k_2+1) \times \cdots \times (k_m+1)$.

No složenost rastava na proste faktore očito je velika, a rezultat za jedan broj ne može se iskoristiti za sljedeće. Zato trebamo drugi pristup.

Pogledajmo svojstva antiprostih brojeva.

1.  Antiprost broj sigurno je produkt potencija uzastopnih prostih brojeva počevši od $2$.

2.  Eksponent manjeg prostog broja veći je ili jednak eksponentu većeg prostog broja, tj. u $n=p_{1}^{k_{1}}p_{2}^{k_{2}} \cdots p_{m}^{k_{m}}$ vrijedi $k_1 \geq k_2 \geq k_3 \geq \cdots \geq k_m$.

Objašnjenje:

1.  Ako prosti brojevi nisu uzastopni počevši od $2$, onda zamjenom nekog prostog broja manjim prostim brojem (uz nepromijenjene eksponente) broj djelitelja ostaje isti, ali vrijednost $n$ postaje manja. Vrijednost $n$ najmanja je kada su prosti brojevi uzastopni počevši od $2$.

2.  Ako je eksponent manjeg prostog broja manji od eksponenta većeg, zamjenom mjesta tih dvaju prostih brojeva (uz nepromijenjene eksponente) broj djelitelja dobivenog $n$ ostaje isti, a vrijednost $n$ postaje manja.

Ostaju još dva pitanja:

1.  Za zadani $n$, do kojeg prostog broja treba ići?

    U najekstremnijem slučaju $n=p_{1}p_{2} \cdots p_{m}$, pa je dovoljno množiti uzastopne proste brojeve dok je produkt još manji ili jednak $n$. Ako bismo išli do većeg prostog broja, to bi značilo da je eksponent nekog prethodnog prostog broja nužno $0$, pa broj ne može biti antiprost.

2.  Do kojeg eksponenta treba ići?

    Razmotrimo ekstreman slučaj: kad je neka potencija najmanjeg prostog broja već veća od zadanog $n$ (od njegove najveće vrijednosti), u svakom drugom obliku rastava najveći eksponent sigurno je manji od tog eksponenta. U ekstremnom slučaju $n$ je potencija broja $2$, pa je dovoljno ići do $\lfloor\log_2 n\rfloor$.

Detalji su tu; kako to konkretno implementirati?

Trenutak u kojem dolazimo do svakog prostog broja možemo shvatiti kao korijen stabla, a zatim pretraživati razinu po razinu. Kada stati?

1.  Trenutni broj već je veći od traženog;

2.  Trenutni faktor više nije potreban;

3.  Trenutni broj djelitelja veći je od traženog;

4.  Trenutni broj djelitelja upravo je traženi (tada provjeravamo treba li ažurirati najmanji $\mathit{ans}$).

Zatim u DFS-u samo nastavljamo razinu po razinu nabrajati eksponente i iterirati dalje.

### Primjeri zadataka

???+ example "[Codeforces 27E. A number with a given number of divisors](https://codeforces.com/problemset/problem/27/E)"
    Nađite najmanji prirodni broj sa zadanim brojem djelitelja. Odgovor zajamčeno ne prelazi $10^{18}$.

??? note "Ideja rješenja"
    Za ovakve zadatke dovoljno je kao uvjet povratka iz DFS-a uzeti broj djelitelja i stalno ažurirati najmanju pronađenu vrijednost.

??? note "Referentni kod"
    ```cpp
    --8<-- "docs/math/code/prime/prime_1.cpp"
    ```

???+ example "[ZOJ 2562 More Divisors](https://pintia.cn/problem-sets/91827364500/exam/problems/type/7?problemSetProblemId=91827366061)"
    Među brojevima koji ne prelaze $n$ nađite onaj s najviše djelitelja.

??? note "Ideja rješenja"
    Ideja je ista kao gore, samo treba promijeniti uvjet povratka iz DFS-a. Pazite na raspon podataka u ovakvim zadacima: 32-bitni cijeli brojevi mogu prekoračiti.

??? note "Referentni kod"
    ```cpp
    --8<-- "docs/math/code/prime/prime_2.cpp"
    ```

## Literatura i bilješke

1.  Rui-Juan Jing, Marc Moreno-Maza, Delaram Talaashrafi, "[Complexity Estimates for Fourier-Motzkin Elimination](https://arxiv.org/abs/1811.01510)", Journal of Functional Programming 16:2 (2006) pp 197-217.
2.  [数论部分第一节：素数与素性测试 (Teorija brojeva, 1. odjeljak: prosti brojevi i testovi prostosti)](http://www.matrix67.com/blog/archives/234)
3.  [Miller–Rabin 与 Pollard–Rho 学习笔记 (Bilješke o Miller–Rabinu i Pollard–Rhou) - Bill Yang's Blog](https://blog.bill.moe/miller-rabin-notes/)
4.  [Primality test - Wikipedia](https://en.wikipedia.org/wiki/Primality_test)
5.  [Fermat pseudoprime - Wikipedia](https://en.wikipedia.org/wiki/Fermat_pseudoprime)
6.  [桃子的算法笔记——反素数详解（acm/OI）(Taozijeve bilješke o algoritmima – antiprosti brojevi detaljno (acm/OI))](https://zhuanlan.zhihu.com/p/41759808)
7.  [The Rabin-Miller Primality Test](http://home.sandiego.edu/~dhoffoss/teaching/cryptography/10-Rabin-Miller.pdf)
8.  [Highly composite number - Wikipedia](https://en.wikipedia.org/wiki/Highly_composite_number)

[^inf-fermat-pp]: Teorem 1 u Pomerance, Carl, John L. Selfridge, and Samuel S. Wagstaff. "The pseudoprimes to 25⋅ 10⁹." Mathematics of Computation 35, no. 151 (1980): 1003-1026. pokazuje da za fiksnu bazu $a$ postoji beskonačno mnogo složenih brojeva koji prolaze i jači Miller–Rabinov test prostosti.

[^millerrabinproof]: Ova tvrdnja i njezin dokaz slijede odjeljak 3.5 knjige Crandall, Richard, and Carl Pomerance. Prime numbers: a computational perspective. New York, NY: Springer New York, 2005.

[^deterministic-proof]: Bach, Eric , "[Explicit bounds for primality testing and related problems](https://doi.org/10.2307%2F2008811)", Mathematics of Computation, 55:191 (1990) pp 355–380.

[^witnesses]: Više sličnih rezultata vidi u [Deterministic variant of the Miller–Rabin primality test](https://miller-rabin.appspot.com/#).
