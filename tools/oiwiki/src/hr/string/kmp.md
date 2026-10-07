---
title: Prefiksna funkcija i KMP algoritam
---

## Definicija prefiksa i sufiksa stringa

Definicije prefiksa, pravog prefiksa, sufiksa i pravog sufiksa stringa nalaze se na stranici [Osnove stringova](./basic.md).

## Prefiksna funkcija

### Definicija

Za string $s$ duljine $n$ njegova se **prefiksna funkcija** (prefix function) definira kao niz $\pi$ duljine $n$.
Pritom je $\pi[i]$ definiran ovako:

1.  ako podstring $s[0\dots i]$ ima par jednakih pravih prefiksa i pravih sufiksa, $s[0\dots k-1]$ i $s[i - (k - 1) \dots i]$, onda je $\pi[i]$ duljina tog pravog prefiksa (ili pravog sufiksa, jer su jednaki), tj. $\pi[i]=k$;
2.  ako takvih parova ima više, $\pi[i]$ je duljina najduljeg među njima;
3.  ako jednakih nema, $\pi[i]=0$.

Jednostavno rečeno, $\pi[i]$ je duljina najduljeg jednakog pravog prefiksa i pravog sufiksa podstringa $s[0\dots i]$.

Matematičkim jezikom:

$$
\pi[i] = \max_{k = 0 \dots i}\{k: s[0 \dots k - 1] = s[i - (k - 1) \dots i]\}
$$

Posebno, dogovorno je $\pi[0]=0$.

### Postupak

Primjerice, za string `abcabcd`:

$\pi[0]=0$, jer `a` nema pravi prefiks ni pravi sufiks, pa je po dogovoru 0

$\pi[1]=0$, jer `ab` nema jednakih pravih prefiksa i pravih sufiksa

$\pi[2]=0$, jer `abc` nema jednakih pravih prefiksa i pravih sufiksa

$\pi[3]=1$, jer `abca` ima samo jedan par jednakih pravih prefiksa i pravih sufiksa: `a`, duljine 1

$\pi[4]=2$, jer je jedini jednaki pravi prefiks i pravi sufiks stringa `abcab` upravo `ab`, duljine 2

$\pi[5]=3$, jer je jedini jednaki pravi prefiks i pravi sufiks stringa `abcabc` upravo `abc`, duljine 3

$\pi[6]=0$, jer `abcabcd` nema jednakih pravih prefiksa i pravih sufiksa

Na isti način izračunamo da je prefiksna funkcija stringa `aabaaab` jednaka $[0, 1, 0, 1, 2, 2, 3]$.

## Naivni algoritam za računanje prefiksne funkcije

### Postupak

Algoritam koji prefiksnu funkciju računa izravno po definiciji teče ovako:

-   u petlji redom za $i = 1\to n - 1$ računamo vrijednost prefiksne funkcije $\pi[i]$ ($\pi[0]$ postavimo na $0$);
-   da bismo izračunali trenutnu vrijednost $\pi[i]$, varijablom $j$ krećemo od najveće moguće duljine pravog prefiksa, $i$;
-   ako su pri trenutnoj duljini pravi prefiks i pravi sufiks jednaki, ta je duljina $\pi[i]$; inače smanjimo $j$ za 1 i nastavimo uspoređivati sve dok $j=0$;
-   ako je $j = 0$ i još nije bilo nijednog podudaranja, postavimo $\pi[i] = 0$ i prijeđemo na sljedeći indeks $i + 1$.

???+ note "Implementacija"
    Konkretna implementacija:
    
    === "C++"
        ```cpp
        // Napomena:
        // string substr (size_t pos = 0, size_t len = npos) const;
        vector<int> prefix_function(string s) {
          int n = (int)s.length();
          vector<int> pi(n);
          for (int i = 1; i < n; i++)
            for (int j = i; j >= 0; j--)
              if (s.substr(0, j) == s.substr(i - j + 1, j)) {
                pi[i] = j;
                break;
              }
          return pi;
        }
        ```
    
    === "Python"
        ```python
        def prefix_function(s):
            n = len(s)
            pi = [0] * n
            for i in range(1, n):
                for j in range(i, -1, -1):
                    if s[0:j] == s[i - j + 1 : i + 1]:
                        pi[i] = j
                        break
            return pi
        ```
    
    === "Java"
        ```java
        static int[] prefix_function(String s) {
            int n = s.length();
            int[] pi = new int[n];
            for (int i = 1; i < n; i++) {
                for (int j = i; j >= 0; j--) {
                    if (s.substring(0, j).equals(s.substring(i - j + 1, i + 1))) {
                        pi[i] = j;
                        break;
                    }
                }
            }
            return pi;
        }
        ```

Očito je vremenska složenost ovog algoritma $O(n^3)$, pa ima mnogo prostora za poboljšanje.

## Učinkovit algoritam za računanje prefiksne funkcije

### Prva optimizacija

Prvo važno zapažanje: **susjedne vrijednosti prefiksne funkcije rastu za najviše $1$**.

Pogledajmo sliku u nastavku i razmislimo ovako: ako želimo što veći $\pi[i+1]$, novi znak $s[i+1]$ nužno se mora podudarati sa znakom koji mu odgovara, tj. $s[i+1]=s[\pi[i]]$, i tada je $\pi[i+1] = \pi[i]+1$.

$$
\underbrace{\overbrace{s_0 ~ s_1 ~ s_2}^{\pi[i] = 3} ~ s_3}_{\pi[i+1] = 4} ~ \dots ~ \underbrace{\overbrace{s_{i-2} ~ s_{i-1} ~ s_{i}}^{\pi[i] = 3} ~ s_{i+1}}_{\pi[i+1] = 4}
$$

Dakle, pri prelasku na sljedeću poziciju vrijednost prefiksne funkcije ili poraste za jedan, ili ostane ista, ili se smanji.

???+ note "Implementacija"
    Ovako poboljšan algoritam:
    
    === "C++"
        ```cpp
        vector<int> prefix_function(string s) {
          int n = (int)s.length();
          vector<int> pi(n);
          for (int i = 1; i < n; i++)
            for (int j = pi[i - 1] + 1; j >= 0; j--)  // improved: j=i => j=pi[i-1]+1
              if (s.substr(0, j) == s.substr(i - j + 1, j)) {
                pi[i] = j;
                break;
              }
          return pi;
        }
        ```
    
    === "Python"
        ```python
        def prefix_function(s):
            n = len(s)
            pi = [0] * n
            for i in range(1, n):
                for j in range(pi[i - 1] + 1, -1, -1):
                    if s[0:j] == s[i - j + 1 : i + 1]:
                        pi[i] = j
                        break
            return pi
        ```
    
    === "Java"
        ```java
        static int[] prefix_function(String s) {
            int n = s.length();
            int[] pi = new int[n];
            for (int i = 1; i < n; i++) {
                for (int j = pi[i - 1] + 1; j >= 0; j--) {
                    if (s.substring(0, j).equals(s.substring(i - j + 1, i + 1))) {
                        pi[i] = j;
                        break;
                    }
                }
            }
            return pi;
        }
        ```

U ovom prvom poboljšanju algoritma najbolji je slučaj pri računanju svakog $\pi[i]$ da već prva usporedba stringova uspije, tj. osnovni broj usporedbi stringova iznosi $n-1$.

Budući da `j = pi[i-1]+1` (uz `pi[0]=0`) ograničava najveći broj usporedbi stringova, vidimo da se gornja granica broja usporedbi povećava za $1$ samo u najboljem slučaju, dok svaka usporedba više od jedne troši prostor za kasniji rast.

Odatle dobivamo slučaj s najviše usporedbi stringova: barem $1$ potrošena usporedba i najviše $n-2$ akumuliranih usporedbi, pa je ukupan broj usporedbi stringova $n-1 + n-2 = 2n-3$.

Vidimo da je nakon ove optimizacije za računanje prefiksne funkcije potrebno samo $O(n)$ usporedbi stringova, pa ukupna složenost pada na $O(n^2)$.

### Druga optimizacija

U prvoj optimizaciji razmotrili smo najbolji slučaj pri računanju $\pi[i+1]$: $s[i+1]=s[\pi[i]]$, kad je $\pi[i+1] = \pi[i]+1$. Pođimo sad tim putem malo dalje i razmotrimo kamo skočiti kad je $s[i+1] \neq s[\pi[i]]$.

![](images/prefix_str_1.svg)

Kao na slici, pri nepodudaranju želimo za podstring $s[0\dots i]$ pronaći drugu najveću duljinu $j$, odmah iza $\pi[i]$, za koju prefiksno svojstvo na poziciji $i$ i dalje vrijedi, tj. $s[0 \dots j - 1] = s[i - j + 1 \dots i]$:

$$
\overbrace{\underbrace{s_0 ~ s_1}_j ~ s_2 ~ s_3}^{\pi[i]} ~ \dots ~ \overbrace{s_{i-3} ~ s_{i-2} ~ \underbrace{s_{i-1} ~ s_{i}}_j}^{\pi[i]} ~ s_{i+1}
$$

Ako pronađemo takvu duljinu $j$, dovoljno je ponovno usporediti $s[i + 1]$ i $s[j]$. Ako su jednaki, onda je $\pi[i + 1] = j + 1$. Inače moramo za podstring $s[0\dots i]$ pronaći sljedeću najveću duljinu $j^{(2)}$ nakon $j$ za koju prefiksno svojstvo vrijedi, i tako dalje sve dok $j = 0$. Ako je $s[i + 1] \neq s[0]$, onda je $\pi[i + 1] = 0$. Shema druge usporedbe prikazana je na sljedećoj slici

![](images/prefix_str_2.svg)

Promatrajući sliku vidimo da zbog $s[0\dots \pi[i]-1] = s[i-\pi[i]+1\dots i]$ druga najveća duljina $j$ podstringa $s[0\dots i]$ ima ovo svojstvo:

$$
s[0 \dots j - 1] = s[i - j + 1 \dots i]= s[\pi[i]-j\dots \pi[i]-1]
$$

Shema te formule prikazana je na sljedećoj slici:

![](images/prefix_str_3.svg)

Drugim riječima, $j$ je upravo vrijednost prefiksne funkcije podstringa $s[\pi[i]-1]$, što odgovara donjem dijelu slike, tj. $j=\pi[\pi[i]-1]$. Analogno, sljedeća duljina nakon $j$ jednaka je vrijednosti prefiksne funkcije za $s[j-1]$, $j^{(2)}=\pi[j-1]$.

Očito dobivamo rekurziju za $j$: $j^{(n)}=\pi[j^{(n-1)}-1], \ \ (j^{(n-1)}>0)$

### Konačni algoritam

Tako konačno dobivamo algoritam koji ne radi nijednu usporedbu stringova i izvodi samo $O(n)$ operacija.

Štoviše, implementacija je iznenađujuće kratka i jasna:

???+ note "Implementacija"
    === "C++"
        ```cpp
        vector<int> prefix_function(string s) {
          int n = (int)s.length();
          vector<int> pi(n);
          for (int i = 1; i < n; i++) {
            int j = pi[i - 1];
            while (j > 0 && s[i] != s[j]) j = pi[j - 1];
            if (s[i] == s[j]) j++;
            pi[i] = j;
          }
          return pi;
        }
        ```
    
    === "Python"
        ```python
        def prefix_function(s):
            n = len(s)
            pi = [0] * n
            for i in range(1, n):
                j = pi[i - 1]
                while j > 0 and s[i] != s[j]:
                    j = pi[j - 1]
                if s[i] == s[j]:
                    j += 1
                pi[i] = j
            return pi
        ```
    
    === "Java"
        ```java
        static int[] prefix_function(String s) {
            int n = s.length();
            int[] pi = new int[n];
            for (int i = 1; i < n; i++) {
                int j = pi[i - 1];
                while (j > 0 && s.charAt(i) != s.charAt(j)) {
                    j = pi[j - 1];
                }
                if (s.charAt(i) == s.charAt(j)) {
                    j++;
                }
                pi[i] = j;
            }
            return pi;
        }
        ```

Ovo je **online** algoritam, tj. obrađuje podatke kako pristižu – primjerice, string možemo čitati znak po znak i odmah ga obrađivati te za svaki znak izračunati vrijednost prefiksne funkcije. Algoritam i dalje mora pohraniti sam string i prethodno izračunate vrijednosti prefiksne funkcije, ali ako unaprijed znamo najveću moguću vrijednost $M$ prefiksne funkcije tog stringa, dovoljno je pohraniti samo prvih $M + 1$ znakova stringa i pripadne vrijednosti prefiksne funkcije.

## Primjene

### Traženje podstringa u stringu: Knuth–Morris–Prattov algoritam

Algoritam su 1977. zajedno objavili Knuth, Pratt i Morris[^kmp]. Ovaj je zadatak tipična primjena prefiksne funkcije.

#### Postupak

Zadani su tekst $t$ i string $s$; želimo pronaći i ispisati sva pojavljivanja (occurrence) stringa $s$ u $t$.

Radi jednostavnosti duljinu stringa $s$ označimo s $n$, a duljinu teksta $t$ s $m$.

Konstruiramo string $s + \# + t$, gdje je $\#$ separator koji se ne pojavljuje ni u $s$ ni u $t$. Zatim izračunamo prefiksnu funkciju tog stringa. Razmotrimo sada značenje vrijednosti prefiksne funkcije nakon prvih $n + 1$ vrijednosti (onih koje pripadaju stringu $s$ i separatoru). Po definiciji je $\pi[i]$ duljina najduljeg pravog podstringa koji završava na poziciji $i$ i ujedno je prefiks; u našem je slučaju to duljina najduljeg podstringa koji završava na $i$ i jednak je nekom prefiksu od $s$. Zbog separatora ta duljina ne može premašiti $n$. Ako pak vrijedi $\pi[i] = n$, to znači da se $s$ u cijelosti pojavljuje na tom mjestu (tj. njegov je desni kraj na poziciji $i$). Uočimo da se taj indeks odnosi na string $s + \# + t$.

Dakle, ako na nekoj poziciji $i$ vrijedi $\pi[i] = n$, string $s$ pojavljuje se u stringu $t$ na poziciji $i - (n - 1) - (n + 1) = i - 2n$. Sljedeća slika prikazuje shemu indeksa.

![](./images/strstr_kmp_indices.svg)

Kao što je već rečeno kod računanja prefiksne funkcije, ako znamo da njezina vrijednost nikad ne premašuje neku granicu, ne moramo pohraniti cijeli string ni cijelu prefiksnu funkciju, nego samo njihov početni dio. U našem slučaju to znači da je dovoljno pohraniti string $s + \#$ i pripadne vrijednosti prefiksne funkcije. String $t$ možemo čitati znak po znak i računati vrijednost prefiksne funkcije na trenutnoj poziciji.

Tako Knuth–Morris–Prattov algoritam (kraće KMP algoritam) rješava problem u vremenu $O(n + m)$ i memoriji $O(n)$.

???+ note "Implementacija"
    === "C++"
        ```cpp
        vector<int> find_occurrences(string text, string pattern) {
          string cur = pattern + '#' + text;
          int sz1 = text.size(), sz2 = pattern.size();
          vector<int> v;
          vector<int> lps = prefix_function(cur);
          for (int i = sz2 + 1; i <= sz1 + sz2; i++) {
            if (lps[i] == sz2) v.push_back(i - 2 * sz2);
          }
          return v;
        }
        ```
    
    === "Python"
        ```python
        def find_occurrences(t, s):
            cur = s + "#" + t
            sz1, sz2 = len(t), len(s)
            ret = []
            lps = prefix_function(cur)
            for i in range(sz2 + 1, sz1 + sz2 + 1):
                if lps[i] == sz2:
                    ret.append(i - 2 * sz2)
            return ret
        ```
    
    === "Java"
        ```java
        static List<Integer> find_occurrences(String text, String pattern) {
            String cur = pattern + '#' + text;
            int sz1 = text.length(), sz2 = pattern.length();
            List<Integer> v = new ArrayList<>();
            int[] lps = prefix_function(cur);
            for (int i = sz2 + 1; i <= sz1 + sz2; i++) {
                if (lps[i] == sz2) {
                    v.add(i - 2 * sz2);
                }
            }
            return v;
        }
        ```

### Period stringa

Za string $s$ i $0 < p \le |s|$ kažemo da je $p$ period stringa $s$ ako $s[i] = s[i+p]$ vrijedi za sve $i \in [0, |s| - p - 1]$.

Za string $s$ i $0 \le r < |s|$, ako su prefiks duljine $r$ i sufiks duljine $r$ stringa $s$ jednaki, prefiks duljine $r$ zovemo border stringa $s$.

Iz toga da $s$ ima border duljine $r$ slijedi da je $|s|-r$ period stringa $s$.

Po definiciji prefiksne funkcije dobivamo duljine svih bordera stringa $s$: $\pi[n-1],\pi[\pi[n-1]-1], \ldots$.[^ref1]

Stoga pomoću prefiksne funkcije u vremenu $O(n)$ možemo izračunati sve periode stringa $s$. Budući da je $\pi[n-1]$ duljina najduljeg bordera od $s$, $n - \pi[n-1]$ je najmanji period stringa $s$.

### Brojanje pojavljivanja svakog prefiksa

U ovom odjeljku razmatramo dva problema istodobno. Zadan je string $s$ duljine $n$; u prvoj inačici problema želimo za svaki prefiks $s[0 \dots i]$ prebrojati njegova pojavljivanja u istom stringu, a u drugoj inačici želimo za svaki prefiks $s[0 \dots i]$ prebrojati pojavljivanja u drugom zadanom stringu $t$.

Riješimo najprije prvi problem. Promotrimo vrijednost prefiksne funkcije $\pi[i]$ na poziciji $i$. Po definiciji to znači da se prefiks stringa $s$ duljine $\pi[i]$ pojavljuje na poziciji $i$ s desnim krajem u $i$, i da ne postoji dulji prefiks s tim svojstvom. Istodobno, kraći prefiksi također mogu završavati na toj poziciji. Lako je vidjeti da smo naišli na pitanje na koje smo već odgovorili pri računanju prefiksne funkcije: ako je zadan prefiks duljine $j$ koji je ujedno sufiks s desnim krajem u $i$, kolika je sljedeća manja duljina $k < j$ prefiksa koji je također sufiks s desnim krajem u $i$? Dakle, s desnim krajem na poziciji $i$ završavaju prefiks duljine $\pi[i]$, prefiks duljine $\pi[\pi[i] - 1]$, prefiks duljine $\pi[\pi[\pi[i] - 1] - 1]$ itd., sve dok duljina ne postane $0$. Odgovor stoga računamo na sljedeći način.

???+ note "Implementacija"
    === "C++"
        ```cpp
        vector<int> ans(n + 1);
        for (int i = 0; i < n; i++) ans[pi[i]]++;
        for (int i = n - 1; i > 0; i--) ans[pi[i - 1]] += ans[i];
        for (int i = 0; i <= n; i++) ans[i]++;
        ```
    
    === "Python"
        ```python
        ans = [0] * (n + 1)
        for i in range(0, n):
            ans[pi[i]] += 1
        for i in range(n - 1, 0, -1):
            ans[pi[i - 1]] += ans[i]
        for i in range(0, n + 1):
            ans[i] += 1
        ```

#### Objašnjenje

U gornjem kodu najprije prebrojimo koliko se puta svaka vrijednost prefiksne funkcije pojavljuje u nizu $\pi$, a zatim računamo konačni odgovor: ako znamo da se prefiks duljine $i$ pojavljuje točno $\text{ans}[i]$ puta, tu vrijednost treba pribrojiti broju pojavljivanja njegova najduljeg podstringa koji je istodobno sufiks i prefiks. Na kraju, da bismo prebrojali i same izvorne prefikse, svakom rezultatu dodamo $1$.

Razmotrimo sada drugi problem. Primijenimo trik iz Knuth–Morris–Pratta: konstruiramo string $s + \# + t$ i izračunamo njegovu prefiksnu funkciju. Jedina razlika u odnosu na prvi problem jest da nas zanimaju samo vrijednosti prefiksne funkcije koje se odnose na string $t$, tj. $\pi[i]$ za $i \ge n + 1$. S tim vrijednostima jednako primijenimo algoritam iz prvog problema.

### Broj različitih podstringova stringa

Zadan je string $s$ duljine $n$; želimo izračunati broj njegovih različitih podstringova.

Problem ćemo riješiti iterativno. Drugim riječima, znajući trenutni broj različitih podstringova, želimo pronaći način da nakon dodavanja jednog znaka na kraj stringa $s$ ponovno izračunamo taj broj.

Neka je $k$ trenutni broj različitih podstringova stringa $s$. Dodajmo novi znak $c$ na kraj od $s$. Očito će se pojaviti neki novi podstringovi koji završavaju znakom $c$. Želimo prebrojati one podstringove koji završavaju tim znakom i koje prije nismo sreli.

Konstruirajmo string $t = s + c$ i obrnimo ga u string $t^{\sim}$. Sada je zadatak izbrojiti koliko se prefiksa od $t^{\sim}$ ne pojavljuje nigdje drugdje u $t^{\sim}$. Ako izračunamo najveću vrijednost prefiksne funkcije od $t^{\sim}$, $\pi_{\max}$, onda najdulji prefiks koji se pojavljuje u $s$ ima duljinu $\pi_{\max}$. Naravno, pojavljuju se i svi kraći prefiksi.

Stoga je broj novih podstringova nakon dodavanja jednog znaka $|s| + 1 - \pi_{\max}$.

Dakle, za svaki dodani znak broj novih podstringova izračunamo u vremenu $O(n)$, pa je ukupna složenost $O(n^2)$.

Vrijedi napomenuti da jednako možemo ponovno izračunati broj različitih podstringova i pri dodavanju znaka na početak te pri uklanjanju znaka s kraja ili s početka.

### Kompresija stringa

Zadan je string $s$ duljine $n$; želimo pronaći njegov najkraći „komprimirani” zapis, tj. tražimo najkraći string $t$ takav da se $s$ može zapisati kao spoj jedne ili više kopija stringa $t$.

Očito je dovoljno pronaći duljinu stringa $t$. Kad znamo tu duljinu, odgovor je prefiks stringa $s$ te duljine.

Izračunajmo prefiksnu funkciju stringa $s$. Pomoću njezine posljednje vrijednosti $\pi[n - 1]$ definiramo $k = n - \pi[n - 1]$. Dokazat ćemo: ako $k$ dijeli $n$, onda je $k$ odgovor; inače valjana kompresija ne postoji, pa je odgovor $n$.

Pretpostavimo da je $n$ djeljiv s $k$. Tada se string može podijeliti na blokove duljine $k$. Po definiciji prefiksne funkcije, prefiks stringa duljine $n - k$ jednak je njegovu sufiksu. No to znači da je posljednji blok jednak pretposljednjem, pretposljednji jednak onome prije njega, itd. Posljedično su svi blokovi jednaki, pa string $s$ možemo komprimirati na duljinu $k$.

???+ note "Dokaz"
    Doduše, još treba dokazati da je ta vrijednost optimalna. Zaista, kad bi postojao komprimirani zapis kraći od $k$, posljednja vrijednost prefiksne funkcije $\pi[n - 1]$ bila bi veća od $n - k$. Dakle, $k$ je odgovor.
    
    Pretpostavimo sada da $n$ nije djeljiv s $k$; kontradikcijom ćemo dokazati da je tada odgovor $n$[^1]. Pretpostavimo da najkraći komprimirani zapis $r$ ima duljinu $p$ ($p$ dijeli $n$) i da je string $s$ podijeljen na $n / p \ge 2$ blokova. Tada posljednja vrijednost prefiksne funkcije $\pi[n - 1]$ mora biti veća od $n - p$ (da je jednaka, $n$ bi bio djeljiv s $k$), tj. sufiks koji ona predstavlja djelomično prekriva prvi blok. Promotrimo sada drugi blok stringa. Taj blok ima dva tumačenja: prvo je $r_0 r_1 \dots r_{p - 1}$, a drugo $r_{p - k} r_{p - k + 1} \dots r_{p - 1} r_0 r_1 \dots r_{p - k - 1}$. Budući da oba tumačenja odgovaraju istom stringu, dobivamo sustav od $p$ jednadžbi koji se kratko zapisuje kao $r_{(i + k) \bmod p} = r_{i \bmod p}$, gdje $\cdot \bmod p$ označava najmanji nenegativni ostatak modulo $p$.
    
    $$
    \begin{gathered}
    \overbrace{r_0 ~ r_1 ~ r_2 ~ r_3 ~ r_4 ~ r_5}^p ~ \overbrace{r_0 ~ r_1 ~ r_2 ~ r_3 ~ r_4 r_5}^p \\
    r_0 ~ r_1 ~ r_2 ~ r_3 ~ \underbrace{\overbrace{r_0 ~ r_1 ~ r_2 ~ r_3 ~ r_4 ~ r_5}^p ~ r_0 ~ r_1}_{\pi[11] = 8}
    \end{gathered}
    $$
    
    Proširenim Euklidovim algoritmom dobivamo $x$ i $y$ takve da je $xk + yp = \gcd(k, p)$. Prikladnim dodavanjem jednakosti $pk - kp = 0$ dobivamo $x' > 0$ i $y' < 0$ takve da je $x'k + y'p = \gcd(k, p)$. To znači da uzastopnom primjenom jednadžbi iz prethodnog sustava dobivamo novi sustav $r_{(i + \gcd(k, p)) \bmod p} = r_{i \bmod p}$.
    
    Budući da $\gcd(k, p)$ dijeli $p$, to znači da je $\gcd(k, p)$ period stringa $r$. A kako je $\pi[n - 1] > n - p$, vrijedi $n - \pi[n - 1] = k < p$, pa je $\gcd(k, p)$ period od $r$ manji od $p$. Dakle, string $s$ ima komprimirani zapis duljine $\gcd(k, p) < p$, što je u suprotnosti s minimalnošću od $p$.
    
    Zaključno, ne postoji komprimirani zapis duljine manje od $k$, pa je odgovor $k$.

[^1]: U ruskoj i engleskoj inačici ovaj dio dokaza čini se pogrešnim. Ovaj dio dokaza dodali su autori ovog članka.

### Izgradnja automata iz prefiksne funkcije

Vratimo se na string nastao spajanjem dvaju stringova preko separatora. Za stringove $s$ i $t$ računamo prefiksnu funkciju od $s + \# + t$. Očito, budući da je $\#$ separator, vrijednost prefiksne funkcije nikad ne premašuje $|s|$. Stoga je dovoljno pohraniti string $s + \#$ i pripadne vrijednosti prefiksne funkcije, a vrijednosti prefiksne funkcije za sve sljedeće znakove možemo računati dinamički:

$$
\underbrace{s_0 ~ s_1 ~ \dots ~ s_{n-1} ~ \#}_{\text{need to store}} ~ \underbrace{t_0 ~ t_1 ~ \dots ~ t_{m-1}}_{\text{do not need to store}}
$$

Zapravo je u tom slučaju za računanje vrijednosti prefiksne funkcije na sljedećoj poziciji dovoljno znati sljedeći znak $c$ stringa $t$ i vrijednost prefiksne funkcije na prethodnoj poziciji; ostali znakovi stringa $t$ i njihove vrijednosti prefiksne funkcije nisu potrebni.

Drugim riječima, možemo izgraditi **automat** (konačni automat): njegova su stanja trenutne vrijednosti prefiksne funkcije, a prijelaz iz jednog stanja u drugo određuje sljedeći znak.

Stoga i bez stringa $t$ možemo algoritmom za izgradnju tablice prijelaza izgraditi tablicu prijelaza $( \text { old } \pi , c ) \rightarrow \text { new } _ { - } \pi$:

???+ note "Implementacija"
    ```cpp
    void compute_automaton(string s, vector<vector<int>>& aut) {
      s += '#';
      int n = s.size();
      vector<int> pi = prefix_function(s);
      aut.assign(n, vector<int>(26));
      for (int i = 0; i < n; i++) {
        for (int c = 0; c < 26; c++) {
          int j = i;
          while (j > 0 && 'a' + c != s[j]) j = pi[j - 1];
          if ('a' + c == s[j]) j++;
          aut[i][c] = j;
        }
      }
    }
    ```

No u ovom obliku, za abecedu malih slova, vremenska složenost algoritma iznosi $O(|\Sigma|n^2)$. Uočimo da dinamičkim programiranjem možemo iskoristiti već izračunate dijelove tablice. Čim prijeđemo s vrijednosti $j$ na $\pi[j - 1]$, zapravo tvrdimo da prijelaz $(j, c)$ vodi u isto stanje kao prijelaz $(\pi[j - 1], c)$, a taj smo odgovor već točno izračunali.

???+ note "Implementacija"
    ```cpp
    void compute_automaton(string s, vector<vector<int>>& aut) {
      s += '#';
      int n = s.size();
      vector<int> pi = prefix_function(s);
      aut.assign(n, vector<int>(26));
      for (int i = 0; i < n; i++) {
        for (int c = 0; c < 26; c++) {
          if (i > 0 && 'a' + c != s[i])
            aut[i][c] = aut[pi[i - 1]][c];
          else
            aut[i][c] = i + ('a' + c == s[i]);
        }
      }
    }
    ```

Konačno, automat možemo izgraditi u vremenskoj složenosti $O(|\Sigma|n)$.

Kada je taj automat koristan? Prvo, sjetimo se da prefiksnu funkciju stringa $s + \# + t$ većinom koristimo s jednim ciljem: pronaći sva pojavljivanja stringa $s$ u stringu $t$.

Stoga je najizravnija korist od automata **ubrzanje računanja prefiksne funkcije stringa $s + \# + t$**.

Izgradnjom automata za $s + \#$ više ne moramo pohranjivati string $s$ ni njegove vrijednosti prefiksne funkcije. Svi su prijelazi već izračunati u tablici.

No osim toga postoji i druga, manje očita primjena. Automatom možemo ubrzati računanje kad je string $t$ **neki golemi string izgrađen po određenim pravilima**. Primjeri su Grayevi stringovi ili string izgrađen rekurzivnim kombiniranjem nekoliko kratkih ulaznih stringova.

Radi potpunosti riješimo ovakav zadatak: zadan je broj $k \le 10^5$ i string $s$ duljine $\le 10^5$; treba izračunati broj pojavljivanja stringa $s$ u $k$-tom Grayevu stringu. Podsjetimo, Grayevi stringovi definirani su ovako:

$$
\begin{aligned}
g_1 &= \mathtt{a}\\
g_2 &= \mathtt{aba}\\
g_3 &= \mathtt{abacaba}\\
g_4 &= \mathtt{abacabadabacaba}
\end{aligned}
$$

Zbog astronomske duljine u ovom slučaju nije moguće čak ni izgraditi string $t$: $k$-ti Grayev string ima $2^k - 1$ znakova. Ipak, znajući samo nekoliko početnih vrijednosti prefiksne funkcije, možemo učinkovito izračunati vrijednost prefiksne funkcije na kraju tog stringa.

Osim automata moramo izračunati i vrijednosti $G[i][j]$: stanje automata nakon obrade $g_i$ počevši iz stanja $j$, te vrijednosti $K[i][j]$: broj pojavljivanja stringa $s$ u $g_i$ kad obradu $g_i$ počnemo iz stanja $j$. Zapravo je $K[i][j]$ broj puta kad je prefiksna funkcija tijekom te obrade poprimila vrijednost $|s|$. Lako se vidi da je odgovor na zadatak $K[k][0]$.

Kako izračunati te vrijednosti? Prvo, po definiciji su početni uvjeti $G[0][j] = j$ i $K[0][j] = 0$. Sve ostale vrijednosti možemo izračunati iz prethodnih vrijednosti pomoću automata. Da bismo izračunali vrijednosti za neki $i$, sjetimo se da je string $g_i$ spoj triju dijelova: $g_{i - 1}$, $i$-tog znaka abecede i $g_{i - 1}$. Stoga automat prolazi kroz sljedeća stanja:

$$
\begin{gathered}
\text{mid} = \text{aut}[G[i - 1][j]][i] \\
G[i][j] = G[i - 1][\text{mid}]
\end{gathered}
$$

Vrijednost $K[i][j]$ također se jednostavno računa.

$$
K[i][j] = K[i - 1][j] + [\text{mid} == |s|] + K[i - 1][\text{mid}]
$$

Pritom je $[\cdot]$ jednako $1$ kad je izraz unutar zagrada istinit, a inače $0$. Time smo riješili zadatak o Grayevim stringovima i velik razred sličnih zadataka. Primjerice, istom se metodom rješava sljedeći zadatak: zadan je string $s$ i neki uzorci $t_i$, pri čemu je svaki uzorak zadan ovako: sastoji se od običnih znakova, među koje se rekurzivno mogu umetnuti prethodni stringovi u obliku $t_{k}^{\text{cnt}}$, tj. na tom mjestu treba umetnuti string $t_k$ $\text{cnt}$ puta. Evo primjera takvih uzoraka:

$$
\begin{aligned}
t_1 &= \mathtt{abdeca} \\
t_2 &= \mathtt{abc} + t_1^{30} + \mathtt{abd} \\
t_3 &= t_2^{50} + t_1^{100} \\
t_4 &= t_2^{10} + t_3^{100}
\end{aligned}
$$

Rekurzivno uvrštavanje uzrokuje eksplozivan rast duljine stringova; njihove duljine mogu dosegnuti i red veličine $100^{100}$. A mi moramo pronaći broj pojavljivanja stringa $s$ u svakom od tih stringova.

I ovaj se zadatak rješava izgradnjom automata iz prefiksne funkcije. Kao i prije, za svaki uzorak izračunamo njegove prijelaze koristeći prethodno izračunate rezultate i odgovarajuće prebrojimo odgovor.

## Zadaci za vježbu

-   [UVa 455 "Periodic Strings"](http://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=396)
-   [UVa 11022 "String Factoring"](http://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=1963)
-   [UVa 11452 "Dancing the Cheeky-Cheeky"](http://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=2447)
-   [UVa 12604 - Caesar Cipher](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=4282)
-   [UVa 12467 - Secret Word](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=3911)
-   [UVa 11019 - Matrix Matcher](https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=1960)
-   [SPOJ - Pattern Find](http://www.spoj.com/problems/NAJPF/)
-   [Codeforces - Anthem of Berland](http://codeforces.com/contest/808/problem/G)
-   [Codeforces - MUH and Cube Walls](http://codeforces.com/problemset/problem/471/D)

## Literatura i bilješke

**Ova je stranica uglavnom prevedena iz članka [Префикс-функция. Алгоритм Кнута-Морриса-Пратта](http://e-maxx.ru/algo/prefix_function) i njegova engleskog prijevoda [Prefix function. Knuth–Morris–Pratt algorithm](https://cp-algorithms.com/string/prefix-function.html). Ruska je inačica objavljena pod licencijom Public Domain + Leave a Link, a engleska pod CC-BY-SA 4.0.**

[^ref1]: [Jin Ce – Odabrana predavanja o algoritmima nad stringovima (kineski)](https://github.com/hzwer/shareOI/blob/master/%E5%AD%97%E7%AC%A6%E4%B8%B2/%E5%AD%97%E7%AC%A6%E4%B8%B2%E7%AE%97%E6%B3%95%E9%80%89%E8%AE%B2_%E9%87%91%E7%AD%96.pdf)

[^kmp]: Knuth, Donald E., James H. Morris, Jr, and Vaughan R. Pratt. "Fast pattern matching in strings." SIAM journal on computing 6.2 (1977): 323-350.[doi: 10.1137/0206024](https://epubs.siam.org/doi/abs/10.1137/0206024)
