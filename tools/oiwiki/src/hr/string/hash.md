---
title: Hashiranje stringova
---

## Definicija

Definiramo funkciju $f$ koja stringove preslikava u cijele brojeve; takva funkcija $f$ zove se hash funkcija.

Želimo da nam ta funkcija $f$ omogući jednostavnu provjeru jesu li dva stringa jednaka.

## Ideja hashiranja

Osnovna ideja hashiranja (hash) jest preslikati ulaz u skup vrijednosti koji je razmjerno malen i u kojem se vrijednosti lako uspoređuju.

??? warning "Upozorenje"
    „Razmjerno malen skup vrijednosti” znači različite stvari u različitim situacijama.
    
    Kod [hash tablice](../ds/hash.md) skup vrijednosti mora biti dovoljno malen da je prihvatljiva linearna prostorna i vremenska složenost.
    
    Kod hashiranja stringova skup vrijednosti mora biti dovoljno malen da se vrijednosti mogu brzo uspoređivati (i $10^9$ i $10^{18}$ brzo se uspoređuju).
    
    Istodobno, da bi se smanjila učestalost kolizija, skup vrijednosti ne smije biti ni premalen.

## Svojstva

Konkretno, najvažnija svojstva hash funkcije mogu se sažeti u sljedeće dvije točke:

1.  ako su hash vrijednosti različite, stringovi su sigurno različiti;

2.  ako su hash vrijednosti jednake, stringovi nisu nužno jednaki (ali su jednaki s velikom vjerojatnošću, a mi se, naravno, nadamo da su uvijek jednaki).

    Pojavu da su hash vrijednosti jednake, a izvorni stringovi različiti, zovemo hash kolizijom.

## Objašnjenje

Na što trebamo paziti?

Na vremensku složenost i na točnost hasha.

Obično koristimo polinomni hash: za string $s$ duljine $l$ polinomnu hash funkciju možemo definirati ovako: $f(s) = \sum_{i=1}^{l} s[i] \times b^{l-i} \pmod M$. Na primjer, za string $xyz$ hash vrijednost je $xb^2+yb+z$.

Posebno napominjemo da mnogi koriste i drugu definiciju hash funkcije, $f(s) = \sum_{i=1}^{l} s[i] \times b^{i-1} \pmod M$; po toj definiciji hash istog stringa $xyz$ postaje $x+yb+zb^2$.

Očito su obje definicije hash funkcije upotrebljive, ali formule za računanje hasha podstringa, o čemu će biti riječi kasnije, za njih su različite, pa svakako pazite da **ne pomiješate ta dva načina hashiranja**.

Budući da se prva definicija jednostavnije računa, više se koristi i može se, radi lakšeg razumijevanja, shvatiti kao broj u bazi $b$, u nastavku ovog članka razmatramo isključivo hash funkciju definiranu s $f(s) = \sum_{i=1}^{l} s[i] \times b^{l-i} \pmod M$.

Osim toga, radi jednostavnosti i radi većeg modula, u C++-u za rezultat hash funkcije ponekad koristimo tip `unsigned long long`. Zbog svojstava C++-a to je isto kao da smo za modul $M$ uzeli $2^{64}$, što je također dobar izbor.

O točnosti ćemo govoriti kasnije.

## Analiza vjerojatnosti pogreške hasha

### Hash kolizija

Hash kolizija znači da se dva različita stringa preslikavaju u istu hash vrijednost.

Neka je $d$ veličina prostora hash vrijednosti (broj svih mogućih vrijednosti), a $n$ broj izračuna (broj stringova koje hashiramo).

Tada je vjerojatnost hash kolizije:

$$
p(n,d) = 1 - \frac{d!}{d^n\left(d-n\right)!} \approx 1 - \exp(-\frac{n(n-1)}{2d} )
$$

??? note "Dokaz"
    Ako su sve hash vrijednosti jednako vjerojatne, vjerojatnost da nema kolizije je:
    
    $$
    \overline{p}(n,d) = 1 \cdot \left (1 - \frac{1}{d} \right) \cdot \left ( 1- \frac{2}{d}\right) \cdots \left ( 1- \frac{n-1}{d}\right)
    $$
    
    Sređivanjem dobivamo:
    
    $$
    \begin{aligned}
    \overline{p}(n,d) 
    & = \frac{d}{d}\cdot \frac{d-1}{d}\cdot \frac{d-2}{d} \cdots \frac{d-n+1}{d}\\
    & = \frac{d\cdot (d-1)\cdot (d-2)\cdots(d-n+1)}{d^n}\\
    & = \frac{d!}{d^n\left(d-n\right)!}
    \end{aligned}
    $$
    
    Dakle, vjerojatnost hash kolizije je:
    
    $$
    p(n,d) = 1 - \frac{d!}{d^n\left(d-n\right)!}
    $$
    
    Ova je formula još uvijek presložena, pa je dodatno pojednostavnimo.
    
    Prema Taylorovoj formuli:
    
    $$
    \exp(x) = \sum_{k=0}^{\infty}\frac{x^k}{k!}=1+x+\frac{x^2}{2}+\frac{x^3}{6}+\frac{x^4}{24}+\cdots
    $$
    
    Kad je $x$ vrlo malen, $\exp(x)$ se približava $1+x$.
    
    Uvrstimo to u izvornu formulu za vjerojatnost da nema kolizije:
    
    $$
    \overline{p}(n,d) \approx 1 \cdot \exp(-\frac{1}{d}) \cdot \exp(-\frac{2}{d}) \cdots \exp(-\frac{n-1}{d})
    $$
    
    Sređivanjem:
    
    $$
    \begin{aligned}
    \overline{p}(n,d) & \approx \exp(-\frac{1}{d} - \frac{2}{d} - \cdots -\frac{n-1}{d})\\
    &=\exp(-\frac{n(n-1)}{2d} )
    \end{aligned}
    $$
    
    Dakle, vjerojatnost hash kolizije je:
    
    $$
    p(n,d) \approx 1 - \exp(-\frac{n(n-1)}{2d})
    $$

### Rušenje hasha s velikim modulom

Promotrimo ovu formulu:

$$
p(n,d) \approx 1 - \exp(-\frac{n(n-1)}{2d} )
$$

Da bismo „srušili” hash (izazvali koliziju), moraju biti ispunjeni sljedeći uvjeti:

1.  $d$ mora biti veći od modula.
2.  $1-p(d,n)$ mora biti što manji.

Primjer:

Ako je abeceda skup **velikih i malih slova te znamenki**, a modul je $10^9+7$:

$\log_{62}10^9+7\approx 6$

$p(10^6,62^{6}) \approx 0.9$

Dakle, za ovaj raspon, ako nasumično generiramo $10^6$ stringova duljine $6$, vjerojatnost da dva od njih imaju istu hash vrijednost čak je $90\%$.

### Rušenje hasha s prirodnim prekoračenjem

Zbog prevelikog modula ovaj se hash ne može srušiti gornjom metodom, pa nam treba druga metoda.

Prvo, ovaj hash ima oblik $f(s) = \sum_{i=1}^{l} s[i] \times b^{l-i}$; razmatramo slučajeve prema $b$.

#### Paran b

Tada je $f(s) = s_1\cdot b^l + s_2\cdot b^{l-1} + \cdots + s_l\cdot b \pmod M$, gdje je $M$ jednak $2^{64}$.

Lako se vidi da za $l \ge 64$ vrijedi $s_i\cdot b^l \equiv 0 \pmod M$.

Dakle, dovoljno je konstruirati stringove oblika:

`aaa...a`

`baa...a`

duljine veće od $64$ i dobit ćemo koliziju.

#### Neparan b

Definiramo $!s_i$ kao string $s_i$ u kojem su svi znakovi zamijenjeni suprotnima.

Primjer:

$s_i = abaab$

$!s_i = babba$

tj. `a` postaje `b`, a `b` postaje `a`.

Nadalje definiramo $hash_i$ kao hash vrijednost stringa $s_i$, a $!hash_i$ kao hash vrijednost stringa $!s_i$.

Uzastopno konstruiramo $s_i = s_{i-1} + !s_{i-1}$.

$s_{12}$ i $!s_{12}$ upravo su dva stringa koja tražimo.

??? note "Izvod"
    Prvo, vrijedi:
    
    $$
    \begin{aligned}
    hash_i = hash_{i-1}\cdot base^{2^{i-2}} + !hash_{i-1}\\
    !hash_{i} = !hash_{i-1}\cdot base^{2^{i-2}}+hash_{i-1}
    \end{aligned}
    $$
    
    Pokušajmo oduzeti:
    
    $$
    \begin{aligned}
    &hash_i - !hash_i\\
    =\ &hash_{i-1}\cdot base^{2^{i-2}} + !hash_{i-1}-(!hash_{i-1}\cdot base^{2^{i-2}}+hash_{i-1})\\
    =\ &(hash_{i-1}-!hash_{i-1})\cdot (base^{2^{i-2}}-1)
    \end{aligned}
    $$
    
    Pojavio se $2^i$, ali je izvorni izraz presložen, pa pokušajmo sa supstitucijom:
    
    Neka je:
    
    $$
    \begin{aligned}
    f_i = hash_i - !hash_i\\
    g_i = base^{2^{i-2}}-1
    \end{aligned}
    $$
    
    Iz izvornog izraza dobivamo:
    
    $$
    \begin{aligned}
    f_i &= f_{i-1} \cdot g_i\\
        &=f_1 \cdot g_1 \cdot g_2 \cdots g_{i-1}\\
    \end{aligned}
    $$
    
    Budući da je $base^{2^{i-2}}$ sigurno neparan, $g_i$ je sigurno paran.
    
    Stoga:
    
    $$
    2^{i-1} | f_i
    $$
    
    No to je prevelik zahtjev: trebalo bi $i-1\ge 64$ da bismo srušili hash; pojednostavnimo dalje:
    
    $$
    g_i = base^{2^{i-2}}-1 = (base^{2^{i-3}}-1)\cdot(base^{2^{i-3}}+1)\\
    $$
    
    tj. $g_i$ je oblika $g_{i-1} \cdot c\ (c \equiv 0 \pmod 2)$.
    
    Dakle $2 | s_1$, $4 | s_2$, …, tj.
    
    $$
    \begin{aligned}
    & 2^i &| g_i\\
    &2^1\cdot2^2\cdot2^3\cdots2^{i-1} &| f_i\\
    &2^{i(i-1)/2} &| f_i
    \end{aligned}
    $$
    
    tj. već za $i=12$ postižemo $2^{64} | hash_i - !hash_i$, što je i trebalo.

### Primjeri zadataka

???+ note "[Primjer: BZOJ 3097 Hash Killer I](https://hydro.ac/p/bzoj-P3097)"
    Zadan je hash implementiran **prirodnim prekoračenjem**; treba konstruirati string koji ga ruši.

???+ note "[Primjer: BZOJ 3097 Hash Killer II](https://hydro.ac/p/bzoj-P3098)"
    Zadan je hash implementiran **velikim modulom**; treba konstruirati string koji ga ruši.

???+ note "[Primjer: Luogu U461211 Hash stringova (pojačani testovi)](https://www.luogu.com.cn/problem/U461211)"
    Zadano je $n$ stringova; odredi koliko je među njima različitih.

## Poboljšanja hasha

### Višestruki hash

Nakon tolikih načina rušenja, naravno, postoje i rješenja.

Višestruki hash znači da imamo više hash funkcija, svaku s drugim modulom; time rješavamo problem hash kolizija.

Pri provjeri, čim se jedna od hash vrijednosti razlikuje, smatramo da su stringovi različiti; ako su sve hash vrijednosti jednake, smatramo da su stringovi jednaki.

Općenito je dvostruki hash dovoljan.

### Više upita na hash podstringa

Jednokratno računanje hash vrijednosti stringa ima složenost $O(n)$, gdje je $n$ duljina stringa, što se ne razlikuje od podudaranja grubom silom; ako treba više puta pitati za hash vrijednost podstringa, računanje iznova svaki put vrlo je neučinkovito.

Uobičajeni je pristup unaprijed izračunati hash vrijednost svakog prefiksa cijelog stringa, shvaćajući hash vrijednost kao broj u bazi $b$ uzet modulo $M$; tada se hash svakog podstringa može brzo izračunati:

Neka $f_i(s)$ označava $f(s[1..i])$, tj. hash vrijednost prefiksa duljine $i$ izvornog stringa; po definiciji je $f_i(s)=s[1]\cdot b^{i-1}+s[2]\cdot b^{i-2}+\dots+s[i-1]\cdot b+s[i]$

Sada želimo, na način sličan prefiksnim sumama, brzo izračunati $f(s[l..r])$; po definiciji hash vrijednost stringa $s[l..r]$ je $f(s[l..r])=s[l]\cdot b^{r-l}+s[l+1]\cdot b^{r-l-1}+\dots+s[r-1]\cdot b+s[r]$

Usporedbom ovih dvaju izraza vidimo da vrijedi $f(s[l..r])=f_r(s)-f_{l-1}(s) \times b^{r-l+1}$ (možete provjeriti ručnim uvrštavanjem), pa tom formulom brzo dobivamo hash podstringa. Pritom se $b^{r-l+1}$ može unaprijed izračunati u $O(n)$ i zatim odgovarati na svaki upit u $O(1)$ (naravno, može se i brzim potenciranjem odgovarati u $O(\log n)$ po upitu).

## Implementacija

### Hash s modulom:

Napomena: razmjerno je spor i ne preporučuje se u praksi.

=== "C++"
    ```cpp
    using std::string;
    
    constexpr int M = 1e9 + 7;
    constexpr int B = 233;
    
    using ll = long long;
    
    int get_hash(const string& s) {
      int res = 0;
      for (int i = 0; i < s.size(); ++i) {
        res = ((ll)res * B + s[i]) % M;
      }
      return res;
    }
    
    bool cmp(const string& s, const string& t) {
      return get_hash(s) == get_hash(t);
    }
    ```

=== "Python"
    ```python
    M = int(1e9 + 7)
    B = 233
    
    
    def get_hash(s):
        res = 0
        for char in s:
            res = (res * B + ord(char)) % M
        return res
    
    
    def cmp(s, t):
        return get_hash(s) == get_hash(t)
    ```

### Dvostruki hash:

=== "C++"
    ```cpp
    using ull = unsigned long long;
    ull base = 131;
    ull mod1 = 212370440130137957, mod2 = 1e9 + 7;
    
    ull get_hash1(std::string s) {
      int len = s.size();
      ull ans = 0;
      for (int i = 0; i < len; i++) ans = (ans * base + (ull)s[i]) % mod1;
      return ans;
    }
    
    ull get_hash2(std::string s) {
      int len = s.size();
      ull ans = 0;
      for (int i = 0; i < len; i++) ans = (ans * base + (ull)s[i]) % mod2;
      return ans;
    }
    
    bool cmp(const std::string s, const std::string t) {
      bool f1 = get_hash1(s) != get_hash1(t);
      bool f2 = get_hash2(s) != get_hash2(t);
      return f1 || f2;
    }
    ```

=== "Python"
    ```python
    def get_hash1(s: str) -> int:
        base = 131
        mod1 = 212370440130137957
        ans = 0
        for char in s:
            ans = (ans * base + ord(char)) % mod1
        return ans
    
    
    def get_hash2(s: str) -> int:
        base = 131
        mod2 = 1000000007
        ans = 0
        for char in s:
            ans = (ans * base + ord(char)) % mod2
        return ans
    
    
    def cmp(s: str, t: str) -> bool:
        f1 = get_hash1(s) != get_hash1(t)
        f2 = get_hash2(s) != get_hash2(t)
        return f1 or f2
    ```

## Primjene hasha

### Podudaranje stringova

Izračunamo hash vrijednost uzorka, zatim hash vrijednost svakog podstringa teksta duljine jednake duljini uzorka i usporedimo ih s hash vrijednošću uzorka.

### Podudaranje stringova s dopuštenih $k$ nepodudaranja

Problem: zadan je izvorni string $s$ duljine $n$ i uzorak $p$ duljine $m$; treba odrediti koliko podstringova izvornog stringa odgovara uzorku. $s'$ odgovara $s$ ako i samo ako su $s'$ i $s$ jednake duljine i razlikuju se na najviše $k$ položaja. Pritom je $1\leq n,m\leq 10^6$, $0\leq k\leq 5$.

Ovaj se zadatak ne može riješiti KMP-om, ali se može riješiti kombinacijom hasha i binarnog pretraživanja.

Prolazimo kroz sve podstringove koji bi mogli odgovarati; neka je trenutni podstring $s'$. Hashom i binarnim pretraživanjem brzo nalazimo prvi položaj na kojem se $s'$ i $p$ razlikuju. Zatim iz $s'$ i $p$ odbacimo dio zaključno s tim položajem nepodudaranja i nastavljamo tražiti sljedeće nepodudaranje. Taj se postupak ponavlja najviše $k$ puta.

Ukupna vremenska složenost je $O(m+kn\log_2m)$.

### Najdulji palindromski podstring

Binarno pretražujemo odgovor; pri provjeri izvedivosti prolazimo po središtima palindroma (osima simetrije) i hashom provjeravamo jesu li obje strane jednake. Treba unaprijed izračunati hash vrijednosti i stringa i njegova obrata. Vremenska složenost je $O(n\log n)$.

Ovaj se problem može riješiti u vremenu $O(n)$ [Manacherovim algoritmom](./manacher.md).

Hashom se problem također može riješiti u $O(n)$: neka $R_i$ označava duljinu najduljeg palindroma koji završava na položaju $i$; odgovor je tada $\max_{i=1}^nR_i$. Budući da vrijedi $R_i\leq R_{i-1}+2$, dovoljno je grubom silom krenuti od $R_{i-1}+2$ i smanjivati dok ne nađemo prvi palindrom. Neka varijabla $z$ označava trenutno razmatrani $R_i$, s početnom vrijednošću $0$; tada se $z$ pri svakom povećanju $i$ poveća za $2$, a u svakom koraku petlje grube sile smanji za $1$, pa se petlja izvrši najviše $2n$ puta i ukupna je vremenska složenost $O(n)$.

### Najdulji zajednički podstring

Problem: zadano je $m$ nepraznih stringova ukupne duljine najviše $n$; treba pronaći najdulji zajednički podstring svih stringova, a ako ih ima više, ispisati bilo koji. Pritom je $1\leq m, n\leq 10^6$.

Očito je da ako postoji zajednički podstring duljine $k$, sigurno postoji i zajednički podstring duljine $k-1$. Zato možemo binarno pretraživati duljinu najduljeg zajedničkog podstringa. Neka je trenutna duljina $k$; `check(k)` radi ovako: hashiramo sve podstringove duljine $k$ svakog od stringova i hash vrijednosti spremamo u $n$ hash tablica. Zatim samo tražimo njihov presjek.

Vremenska složenost je $O(m+n\log n)$.

### Određivanje broja različitih podstringova stringa

Problem: zadan je string duljine $n$ sastavljen samo od malih engleskih slova; treba odrediti broj različitih podstringova tog stringa.

Da bismo riješili ovaj problem, prolazimo kroz sve podstringove duljine $l=1,\cdots ,n$. Za svaku duljinu $l$ njihove hash vrijednosti pomnožimo istom potencijom broja $b$ i spremimo u polje. Broj različitih elemenata u polju jednak je broju različitih podstringova te duljine i taj se broj dodaje u konačni odgovor.

Radi praktičnosti koristit ćemo $h [i]$ kao hash prefiksa i definirati $h[0]=0$.

??? note "Referentni kôd"
    ```cpp
    int count_unique_substrings(string const& s) {
      int n = s.size();
    
      constexpr static int b = 31;
      constexpr static int m = 1e9 + 9;
      vector<long long> b_pow(n);
      b_pow[0] = 1;
      for (int i = 1; i < n; i++) b_pow[i] = (b_pow[i - 1] * b) % m;
    
      vector<long long> h(n + 1, 0);
      for (int i = 0; i < n; i++)
        h[i + 1] = (h[i] + (s[i] - 'a' + 1) * b_pow[i]) % m;
    
      int cnt = 0;
      for (int l = 1; l <= n; l++) {
        set<long long> hs;
        for (int i = 0; i <= n - l; i++) {
          long long cur_h = (h[i + l] + m - h[i]) % m;
          cur_h = (cur_h * b_pow[n - i - 1]) % m;
          hs.insert(cur_h);
        }
        cnt += hs.size();
      }
      return cnt;
    }
    ```

### Primjeri zadataka

???+ note "[CF1200E Compress Words](http://codeforces.com/contest/1200/problem/E)"
    Zadano je nekoliko stringova; string-odgovor na početku je prazan. U $i$-tom koraku $i$-ti string nadovezuje se na kraj odgovora, ali tako da se što više ukloni preklapanje (tj. ukloni se najdulji string koji je ujedno sufiks dotadašnjeg odgovora i prefiks $i$-tog stringa). Odredi konačni string.
    
    Stringova je najviše $10^5$, a ukupna duljina najviše $10^6$.
    
    ??? note "Rješenje"
        U svakom koraku treba naći najdulji string koji je ujedno sufiks dotadašnjeg odgovora i prefiks $i$-tog stringa. Prolazimo po duljinama tog stringa i uspoređujemo hashom.
        
        Naravno, zadatak se može riješiti i [KMP algoritmom](./kmp.md).
    
    ??? note "Referentni kôd"
        ```cpp
        --8<-- "docs/string/code/hash/hash_1.cpp"
        ```

**Dio sadržaja ove stranice preveden je iz članka [строковый хеш](https://github.com/e-maxx-eng/e-maxx-eng/blob/61aff51f658644424c5e1b717f14fb7bf054ae80/src/string/string-hashing.md) i njegova engleskog prijevoda [String Hashing](https://cp-algorithms.com/string/string-hashing.html). Ruska je inačica pod licencijom Public Domain + Leave a Link, a engleska pod licencijom CC-BY-SA 4.0.**
