---
title: Rastav na proste faktore
---

## Uvod

Zadan je prirodan broj $N \in \mathbf{N}_{+}$; treba brzo pronaći jedan njegov [netrivijalni djelitelj](./basic.md).

Razmotrimo naivni algoritam. Djelitelji dolaze u parovima, pa se svi djelitelji broja $N$ mogu podijeliti u dva dijela, $[2, \sqrt N]$ i $[\sqrt N+1,N)$. Dovoljno je proći kroz brojeve iz $[2, \sqrt N]$ i zatim dijeljenjem pronaći barem dva djelitelja. Vremenska složenost ove metode jest $O(\sqrt N)$.

Kad je $N\ge10^{18}$, vrijeme izvođenja ovog algoritma za nas je neprihvatljivo, pa želimo bolji algoritam. Jedna je ideja randomizirani pristup: pogađamo je li neki broj djelitelj broja $N$; uz sreću odgovor dobivamo u vremenskoj složenosti $O(1)$, ali za podatke s $N\ge10^{18}$ vjerojatnost uspješnog pogotka iznosi $\frac{1}{10^{18}}$, a očekivani broj pogađanja $10^{18}$. Ako pogađamo unutar $[2,\sqrt N]$, vjerojatnost uspjeha nešto je veća. Želimo metodu kojom ćemo pogađanje optimizirati.

## Naivni algoritam

Najjednostavniji je algoritam prolazak kroz $[2, \sqrt N]$.

=== "C++"
    ```cpp
    vector<int> breakdown(int N) {
      vector<int> result;
      for (int i = 2; i * i <= N; i++) {
        if (N % i == 0) {  // ako i dijeli N, tada je i jedan prosti faktor broja N.
          while (N % i == 0) N /= i;
          result.push_back(i);
        }
      }
      if (N != 1) {  // znači da je nakon svih operacija od N ostao prost broj
        result.push_back(N);
      }
      return result;
    }
    ```

=== "Python"
    ```python
    def breakdown(N):
        result = []
        for i in range(2, int(sqrt(N)) + 1):
            if N % i == 0:  # ako i dijeli N, tada je i jedan prosti faktor broja N.
                while N % i == 0:
                    N //= i
                result.append(i)
        if N != 1:  # znači da je nakon svih operacija od N ostao prost broj
            result.append(N)
        return result
    ```

Možemo dokazati da su svi elementi u `result` upravo svi prosti faktori broja `N`.

??? note "Dokaz da su elementi u `result` upravo svi prosti faktori broja $N$"
    Najprije promotrimo kako se `N` mijenja. Kad završi iteracija petlje za `i`, budući da je upravo izvršen dio `while(N % i == 0) N /= i`, `i` više ne dijeli `N`. Osim toga, svaki put kad uklonimo jedan faktor, `N` i dalje dijeli $N$. Ove dvije činjenice jamče da je na početku iteracije za `i` broj `N` djelitelj broja $N$ koji nije djeljiv nijednim cijelim brojem manjim od `i`.
    
    Zatim dokazujemo da su svi elementi u `result` djelitelji broja $N$. Kad petlja dođe do `i`, uvjet za spremanje `i` u `result` jest `N % i == 0`, što znači da `i` dijeli `N`, a već smo pokazali da je `N` djelitelj broja $N$, pa je i `i` djelitelj broja $N$. Kad petlja po `i` završi, ako `N` nije jednak jedan, i on se sprema u `result`. Prema prethodnome, i on je tada nužno djelitelj broja $N$.
    
    Zatim dokazujemo da su svi elementi u `result` prosti. Pretpostavimo da u `result` postoji složen broj $K$; tada nužno postoji `i` veći od jedan i ne veći od $\sqrt K$ takav da je `i` djelitelj broja $K$. Takav $K$ ne može biti spremljen u `result` kao neki `i` iz petlje, jer je u prvom odlomku pokazano da u trenutku kad petlja dođe do $K$ broj `N` nije djeljiv nijednim `i` manjim od $K$. Takav $K$ ne može biti dodan ni nakon završetka petlje, jer je uvjet izlaska iz petlje `i * i > N`, pa su već obiđeni svi `i` koji ne premašuju $\sqrt K$, a prema rečenome ti `i` nikako ne dijele trenutačni `N`, tj. $K$.
    
    Naposljetku dokazujemo da se svi prosti faktori broja $N$ nužno pojavljuju u `result`. Pretpostavimo da je $p$ prosti faktor broja $N$ koji se ne pojavljuje u `result`. Prema prethodnoj raspravi, $p$ ne može biti neki `i` koji se pojavio u petlji. Neka je `i` posljednji `i` prije izlaska iz petlje; tada je `i` strogo manji od $p$, a `N` nakon izlaska iz petlje nije djeljiv nijednim prethodnim `i`, pa $p$ dijeli `N`. Dakle, završni je `N` veći od jedan, pa je prema prethodnome nužno prost, pa je `N` jednak $p$ i sigurno se na kraju dodaje u `result`, što je u suprotnosti s pretpostavkom.

Vrijedi istaknuti da, ako na početku već imamo pripremljenu tablicu prostih brojeva, vremenska složenost pada s $O(\sqrt N)$ na $O(\frac {\sqrt{N}} {\ln N})$. Više o pripremi tablica pogledajte u odjeljku [Sita](./sieve.md).

Primjer zadatka: [CF 1445C](https://codeforces.com/problemset/problem/1445/C)

## Pollardov rho algoritam

### Uvod

Složenost pronalaženja jednog netrivijalnog djelitelja grubom silom jest $O(p)=O(\sqrt N)$, gdje je $p$ najmanji prosti faktor broja $N$. Pollardov rho algoritam koji ćemo sada predstaviti randomizirani je algoritam koji netrivijalni djelitelj pronalazi u očekivanoj složenosti $O(\sqrt p)=O(N^{1/4})$ (**pozor**: netrivijalni djelitelj ne mora biti prost).

Njegova je ključna ideja sljedeća: za slučajno preslikavanje $f: \mathbf Z_p \rightarrow \mathbf Z_p$ u samog sebe, krenemo li iz bilo koje točke $x_1$ i iterativno računamo $x_n = f(x_{n-1})$, u očekivanom vremenu $O(\sqrt p)$ ulazimo u ciklus. Ako uspijemo pronaći $x_i \equiv x_j \pmod p$, tada $p$ dijeli $\gcd(|x_i-x_j|, N)$, a taj je najveći zajednički djelitelj netrivijalni djelitelj broja $N$.

Za razumijevanje toga zašto je očekivano vrijeme ulaska u ciklus $O(\sqrt p)$ možemo se nadahnuti paradoksom rođendana.

### Paradoks rođendana

Ne uzimajući u obzir godinu rođenja (pretpostavimo da svaka godina ima 365 dana), pitamo: koliko najmanje ljudi mora biti u sobi da bi vjerojatnost da dvoje od njih imaju isti rođendan dosegnula $50\%$?

Rješenje: pretpostavimo da godina ima $n$ dana i da je u sobi $k$ ljudi, koje numeriramo cijelim brojevima $1, 2,\dots, k$. Pretpostavimo da je rođendan svake osobe jednoliko raspodijeljen među $n$ dana te da su rođendani dviju osoba međusobno nezavisni.

Neka je $A$ događaj da svih $k$ ljudi ima međusobno različite rođendane; tada je vjerojatnost događaja $A$

$$
P(A)=\prod_{i=0}^{k-1}\frac{n-i}{n}
$$

Vjerojatnost da barem dvoje ljudi ima isti rođendan jest $P(\overline A)=1-P(A)$. Prema uvjetu zadatka $P(\overline A)\ge\frac{1}{2}$, pa imamo

$$
P(A)=\prod_{i=0}^{k-1}\frac{n-i}{n} \le \frac{1}{2}
$$

Iz nejednakosti $1+x\le \mathrm{e}^x$ dobivamo

$$
P(A) \le \prod_{i=1}^{k-1}\exp\left({-\frac{i}{n}}\right)=\exp \left({-\frac{k(k-1)}{2n}}\right)
$$

Stoga

$$
\exp\left({-\dfrac{k(k-1)}{2n}}\right) \le \frac{1}{2}\implies P(A) \le \frac{1}{2}
$$

Uvrštavanjem $n=365$ dobivamo $k\geq 23$. Dakle, dovoljno je $23$ ljudi u sobi da vjerojatnost da dvoje od njih imaju isti rođendan dosegne $50\%$; budući da je ta matematička činjenica vrlo protuintuitivna, naziva se paradoksom.

Kad je $k>56$ i $n=365$, vjerojatnost da dvoje ljudi imaju rođendan istog dana veća je od $99\%$[^ref1]. Dakle, ako godina ima $n$ dana, kad je u sobi $\frac{1}{2}(\sqrt{8n\ln 2+1}+1)\approx \sqrt{2n\ln 2}$ ljudi, vjerojatnost da barem dvoje imaju isti rođendan iznosi približno $50\%$.

Slično se može izračunati da je, biramo li slučajno i jednoliko niz rođendana, očekivani broj ljudi potreban da se prvi put pojavi ponovljeni rođendan također $O(\sqrt n)$. Označimo li taj broj ljudi s $X$, vrijedi

$$
E(X) = \sum_{x=0}^{n}P(X\ge x+1) = \sum_{x=0}^n\frac{n!}{(n-x)!n^x} = \sqrt{\frac{\pi n}{2}}+\frac23+o(1).
$$

To nas navodi na zaključak da je, ako slučajno biramo niz brojeva, očekivana veličina uzorka potrebna da se pojavi ponovljeni broj također $O(\sqrt n)$.

### Pronalaženje djelitelja pomoću najvećeg zajedničkog djelitelja

Konstruirati niz slučajnih brojeva modulo $p$ u praksi nije moguće, jer je $p$ upravo ono što tražimo. Zato pseudoslučajni niz $\{x_i\}$ generiramo pomoću $f(x)=(x^2+c)\bmod N$: slučajno odaberemo $x_1$ i stavimo $x_2=f(x_1),\ x_3=f(x_2),\ \dots,\ x_i=f(x_{i-1})$, gdje je $c\in[1,N)$ slučajno odabrana konstanta.

Ovdje odabrana funkcija lako se računa i često daje prilično slučajne nizove. No niz nije potpuno slučajan. Na primjer, neka je $N=50,\ c=6,\ x_1=1$; $f(x)$ generira podatke

$$
1, 7, 5, 31, 17, 45, 31, 17, 45, 31,\dots
$$

Vidimo da se podatci nakon $x_4$ ciklički ponavljaju među $31,17,45$. Rasporedimo li te brojeve kao na slici ispod, uočit ćemo da slika nalikuje slovu $\rho$, po čemu je algoritam i dobio ime rho.

![pollard-rho](./images/pollard-rho.svg)

Još je važnije da ovakva funkcija doista daje preslikavanje $\mathbf Z_p$ u samog sebe. Drugim riječima, zadovoljava svojstvo: ako je $x\equiv y\pmod p$, tada je $f(x)\equiv f(y)\pmod p$.

???+ note "Dokaz"
    Ako je $x\equiv y\pmod p$, tada je $x^2+c\equiv y^2+c\pmod p$. Primijetimo da je $f(x)=x^2+c-k_xN$, gdje je $k_x$ cijeli broj koji ovisi o $x$, a $p\mid N$, pa vrijedi $f(x)\equiv x^2+c\pmod p$, dakle $f(x)\equiv f(y)\pmod p$.

Kao niz dobiven uzastopnim iteriranjem pseudoslučajnog preslikavanja $\mathbf Z_p$ u samog sebe, $\{x_n\bmod p\}$ ponovit će se u očekivanom vremenu $O(\sqrt p)$. Čim uočimo takvo ponavljanje $x_i\equiv x_j\pmod p$, iz $\gcd(|x_i-x_j|,N)$ možemo dobiti netrivijalni djelitelj broja $N$. Primijetimo da, budući da je $p$ nepoznat, ne možemo izravno utvrditi je li se ponavljanje dogodilo; jednostavan kriterij upravo je to da je $\gcd(|x_i-x_j|,N)$ strogo veći od jedan.

Ovaj algoritam ne uspijeva uvijek, jer $\gcd(|x_i-x_j|,N)$ može biti jednak $N$. Drugim riječima, $x_i\equiv x_j\pmod N$. Tada se u trenutku kad se $\{x_n\bmod p\}$ prvi put ponovi ponovio i $\{x_n\}$. Nismo dobili netrivijalni djelitelj. Štoviše, nakon što $\{x_n\}$ uđe u ciklus, daljnje iteriranje nema smisla, jer će se dalje samo ponavljati taj ciklus. Algoritam tada treba javiti neuspjeh rastava, a rastav treba ponoviti s drukčije odabranim $c$ u $f(x)$.

Prema gornjoj analizi, teoretski se ovdje može upotrijebiti bilo koja funkcija $f(x)$ koja zadovoljava $\forall x \equiv y \pmod p, f(x) \equiv f(y) \pmod p$ i jamči određenu pseudoslučajnost (na primjer neke polinomne funkcije). U praksi se uglavnom koristi $f(x)=x^2+c\ (c\neq 0,-2)$.[^pseudo]

### Implementacija

Trebamo implementirati algoritam koji tijekom iteriranja brzo utvrđuje je li se $\{x_n\bmod p\}$ već ponovio. Promatramo li $f$ kao bridove usmjerenog grafa čiji su vrhovi elementi $\mathbf Z_p$, zapravo trebamo implementirati algoritam za otkrivanje ciklusa, s tim da provjeru jednakosti zamjenjujemo provjerom je li $\gcd(|x_i-x_j|,N)$ veći od jedan.

#### Floydovo otkrivanje ciklusa

Zamislimo da se dvoje ljudi utrkuje: A je brz, B je spor. Nakon nekog vremena A će sigurno sustići B-a, a u trenutku susreta razlika ukupne udaljenosti koju je prešao A i ukupne udaljenosti koju je prešao B sigurno je višekratnik duljine kruga.

Neka je $a=f(0),b=f(f(0))$; u svakom koraku ažuriramo $a=f(a),b=f(f(b))$ i samo provjeravamo jesu li $a$ i $b$ tijekom ažuriranja postali jednaki; ako jesu, pojavio se ciklus.

U svakom koraku stavimo $d=\gcd(|x_i-x_j|,N)$ i provjerimo zadovoljava li $d$ uvjet $1< d< N$; ako zadovoljava, možemo izravno vratiti $d$. Ako je $d=N$, to znači da je $\{x_i\}$ već zatvorio ciklus; kad se ciklus zatvori, ne može se dalje nastaviti, pa izravno vraćamo sam $N$, a u daljnjem postupku mijenjamo slučajnu konstantu $c$ i ponavljamo rastav.

??? note "Pollardov rho algoritam s Floydovim otkrivanjem ciklusa"
    === "C++"
        ```cpp
        ll Pollard_Rho(ll N) {
          if (N == 4) return 2;  // budući da na početku skačemo dva koraka, 4 treba posebno obraditi
          ll c = rand() % (N - 1) + 1;
          ll t = f(0, c, N);
          ll r = f(f(0, c, N), c, N);
          while (t != r) {
            ll d = gcd(abs(t - r), N);
            if (d > 1) return d;
            t = f(t, c, N);
            r = f(f(r, c, N), c, N);
          }
          return N;
        }
        ```
    
    === "Python"
        ```python
        import random
        
        
        def Pollard_Rho(N):
            if N == 4:
                return 2  # budući da na početku skačemo dva koraka, 4 treba posebno obraditi
            c = random.randint(1, N - 1)
            t = f(0, c, N)
            r = f(f(0, c, N), c, N)
            while t != r:
                d = gcd(abs(t - r), N)
                if d > 1:
                    return d
                t = f(t, c, N)
                r = f(f(r, c, N), c, N)
            return N
        ```

#### Brentovo otkrivanje ciklusa

Zapravo se Floydov algoritam za otkrivanje ciklusa može poboljšati u konstanti. Brentovo otkrivanje ciklusa počinje od $k=1$ i povećava $k$; u $k$-tom krugu A čeka na mjestu, a B se pomiče $2^k$ koraka naprijed. Ako B pritom sretne A-a, ciklus je pronađen; inače A trenutačno premještamo na položaj B-a i prelazimo na sljedeći krug.

Može se dokazati[^brent] da broj poziva funkcije $f$ potrebnih da se tako pronađe ciklus nikad nije veći nego kod Floydova algoritma. Testovi u izvornom radu pokazuju da je prosječno vrijeme Brentova otkrivanja ciklusa za $24\%$ manje od Floydova.

#### Optimizacija udvostručavanjem

Bilo da se koristi Floydovo ili Brentovo otkrivanje ciklusa, broj iteracija jest $O(\sqrt p)$. No računanje $\gcd$ u svakoj iteraciji radi provjere ciklusa usporava algoritam. Broj računanja $\gcd$ može se smanjiti akumuliranjem umnoška.

Jednostavno rečeno, ako je $\gcd(a,N)>1$, tada je $\gcd(ab\bmod N,N)=\gcd(ab,N)>1$ za svaki $b\in\mathbf N_+$. Drugim riječima, ako izračunamo $\gcd(\prod |x_i-x_j| \bmod N,N)>1$, tada nužno neki par $(x_i,x_j)$ zadovoljava $\gcd(|x_i-x_j|,N)>1$. Ako umnožak u nekom trenutku postane nula, rastav nije uspio; izlazimo i vraćamo sam $N$.

Ako $\gcd$ računamo svakih $k$ parova, složenost algoritma pada na $O(\sqrt p+k^{-1}\sqrt p\log N)$, gdje je $\log N$ trošak jednog računanja $\gcd$. Primijetimo da, kad su $k$ i $\log N$ otprilike istog reda veličine, dobivamo očekivanu složenost $O(\sqrt p)$. U konkretnim implementacijama najčešće se uzima $k=127$.

Ovdje dajemo implementaciju Pollardova rho algoritma s Brentovim otkrivanjem ciklusa i optimizacijom udvostručavanjem.

??? note "Implementacija"
    === "C++"
        ```cpp
        ll Pollard_Rho(ll x) {
          ll t = 0;
          ll c = rand() % (x - 1) + 1;
          ll s = t;
          int step = 0, goal = 1;
          ll val = 1;
          for (goal = 1;; goal <<= 1, s = t, val = 1) {
            for (step = 1; step <= goal; ++step) {
              t = f(t, c, x);
              val = val * abs(t - s) % x;
              // ako je val jednak 0, izlazimo i ponavljamo rastav
              if (!val) return x;
              if (step % 127 == 0) {
                ll d = gcd(val, x);
                if (d > 1) return d;
              }
            }
            ll d = gcd(val, x);
            if (d > 1) return d;
          }
        }
        ```
    
    === "Python"
        ```python
        from random import randint
        from math import gcd
        
        
        def Pollard_Rho(x):
            c = randint(1, x - 1)
            s = t = f(0, c, x)
            goal = val = 1
            while True:
                for step in range(1, goal + 1):
                    t = f(t, c, x)
                    val = val * abs(t - s) % x
                    if val == 0:
                        return x  # ako je val jednak 0, izlazimo i ponavljamo rastav
                    if step % 127 == 0:
                        d = gcd(val, x)
                        if d > 1:
                            return d
                d = gcd(val, x)
                if d > 1:
                    return d
                s = t
                goal <<= 1
                val = 1
        ```

#### Složenost

Očekivani broj iteracija u Pollardovu rho algoritmu jest $O(\sqrt p)$, gdje je $p$ najmanji prosti faktor broja $N$. Bez obzira na to koristi li konkretna implementacija Floydovo ili Brentovo otkrivanje ciklusa, bez optimizacije udvostručavanjem očekivana je složenost $O(\sqrt p\log N)$; uz optimizaciju udvostručavanjem dobiva se približno očekivana složenost $O(\sqrt p)$.

Vrijedi spomenuti da se gornja analiza temelji na potpuno slučajnom preslikavanju u samog sebe, dok Pollardov rho algoritam zapravo koristi pseudoslučajnu funkciju, pa algoritam nema strogu analizu složenosti, ali je u praksi obično prilično brz.

#### Primjer zadatka: najveći prosti faktor broja

Primjer zadatka: [P4718【模板】Pollard-Rho 算法 (Predložak: Pollardov rho algoritam)](https://www.luogu.com.cn/problem/P4718)

Za broj $n$ [Miller–Rabinovim algoritmom](./prime.md#millerrabin-素性测试) provjerimo je li prost; ako jest, možemo ga odmah vratiti, a inače Pollardovim rho algoritmom pronađemo djelitelj $p$ i iz $n$ uklonimo faktor $p$. Zatim rekurzivno rastavljamo $n$ i $p$, Miller–Rabinovim testom provjeravamo jesmo li došli do prostog faktora i ažuriramo max\_factor; tako dobivamo najveći prosti faktor. Budući da su podatci u ovom zadatku vrlo veliki, Floydovo otkrivanje ciklusa nije dovoljno, pa ovdje koristimo optimizaciju udvostručavanjem.

??? note "Implementacija"
    ```cpp
    --8<-- "docs/math/code/pollard-rho/pollard-rho_1.cpp"
    ```

## Literatura i poveznice

[^ref1]: <https://en.wikipedia.org/wiki/Birthday_problem#Reverse_problem>

[^pseudo]: Menezes, Alfred J.; van Oorschot, Paul C.; Vanstone, Scott A. (2001). Handbook of Applied Cryptography. Section 3.11 and 3.12.

[^brent]: Brent, R. P. (1980), An improved Monte Carlo factorization algorithm, BIT Numerical Mathematics, 20(2): 176–184, doi:10.1007/BF01933190
