---
title: Sita
---

## Sita za proste brojeve

### Uvod

Što ako želimo znati koliko ima prostih brojeva manjih ili jednakih $n$?

Prirodna je ideja za svaki broj manji ili jednak $n$ provesti po jedan test prostosti. Takav pristup grubom silom očito ne postiže optimalnu složenost.

### Eratostenovo sito

#### Postupak

Razmotrimo sljedeće: za bilo koji prirodan broj $n$ veći od $1$ njegov je $x$-struki višekratnik složen broj ($x > 1$). Pomoću tog zaključka možemo izbjeći mnoge nepotrebne provjere.

Ako brojeve promatramo od manjeg prema većem i pritom sve (od njega veće) višekratnike trenutačnog broja označimo kao složene, tada su na kraju izvođenja neoznačeni brojevi upravo prosti brojevi.

#### Implementacija

=== "C++"
    ```cpp
    vector<int> prime;
    bool is_prime[N];
    
    void Eratosthenes(int n) {
      is_prime[0] = is_prime[1] = false;
      for (int i = 2; i <= n; ++i) is_prime[i] = true;
      for (int i = 2; i <= n; ++i) {
        if (is_prime[i]) {
          prime.push_back(i);
          if ((long long)i * i > n) continue;
          for (int j = i * i; j <= n; j += i)
            // višekratnike brojeva od 2 do i - 1 već smo prosijali, pa ovdje
            // počinjemo izravno od višekratnika broja i, što ubrzava izvođenje
            is_prime[j] = false;  // nijedan višekratnik broja i nije prost
        }
      }
    }
    ```

=== "Python"
    ```python
    prime = []
    is_prime = [False] * N
    
    
    def Eratosthenes(n):
        is_prime[0] = is_prime[1] = False
        for i in range(2, n + 1):
            is_prime[i] = True
        for i in range(2, n + 1):
            if is_prime[i]:
                prime.append(i)
                if i * i > n:
                    continue
                for j in range(i * i, n + 1, i):
                    is_prime[j] = False
    ```

Gore opisani postupak jest **Eratostenovo sito** (sieve of Eratosthenes), vremenske složenosti $O(n\log\log n)$.

???+ note "Dokaz"
    Pogledajmo sada izvod:
    
    Ako svaka operacija nad poljem traje 1 jedinicu vremena, vremenska složenost iznosi:
    
    $$
    O\left(\sum_{k=1}^{\pi(n)}{\frac{n}{p_k}}\right)=O\left(n\sum_{k=1}^{\pi(n)}{\frac{1}{p_k}}\right)
    $$
    
    gdje $p_k$ označava $k$-ti po redu najmanji prosti broj, a $\pi(n)$ broj prostih brojeva $\le n$. $\sum_{k=1}^{\pi(n)}$ predstavlja vanjsku for-petlju, pri čemu je gornja granica zbroja $\pi(n)$ broj ulazaka u granu true uvjeta `if (prime[i])`; $\frac{n}{p_k}$ predstavlja broj izvođenja unutarnje for-petlje.
    
    Prema drugom Mertensovu teoremu postoji konstanta $B_1$ takva da je:
    
    $$
    \sum_{k=1}^{\pi(n)}{\frac{1}{p_k}}=\log\log n+B_1+O\left(\frac{1}{\log n}\right)
    $$
    
    Stoga je vremenska složenost **Eratostenova sita** $O(n\log\log n)$. U nastavku dokazujemo oslabljenu inačicu drugog Mertensova teorema $\sum_{k\le\pi(n)}1/p_k=O(\log\log n)$:
    
    Iz $\pi(n)=\Theta(n/\log n)$ slijedi da je $n$-ti prosti broj veličine $\Theta(n\log n)$. Zato vrijedi
    
    $$
    \begin{aligned}
    \sum_{k=1}^{\pi(n)}{\frac{1}{p_k}}
    &=O\left(\sum_{k=2}^{\pi(n)}{\frac{1}{k\log k}}\right) \\
    &=O\left(\int_2^{\pi(n)}{\frac{\mathrm dx}{x\log x}}\right) \\
    &=O(\log\log\pi(n))=O(\log\log n)
    \end{aligned}
    $$
    
    Naravno, gornji postupak još uvijek nije dovoljno učinkovit; primjenom sljedećih nekoliko metoda može se nešto povećati učinkovitost izvođenja algoritma.

#### Prosijavanje do korijena

Očito je da je za pronalaženje svih prostih brojeva do $n$ dovoljno prosijavati samo prostim brojevima koji ne premašuju $\sqrt n$.

=== "C++"
    ```cpp
    vector<int> prime;
    bool is_prime[N];
    
    void Eratosthenes(int n) {
      is_prime[0] = is_prime[1] = false;
      for (int i = 2; i <= n; ++i) is_prime[i] = true;
      // i * i <= n znači i <= sqrt(n)
      for (int i = 2; i * i <= n; ++i) {
        if (is_prime[i])
          for (int j = i * i; j <= n; j += i) is_prime[j] = false;
      }
      for (int i = 2; i <= n; ++i)
        if (is_prime[i]) prime.push_back(i);
    }
    ```

=== "Python"
    ```python
    prime = []
    is_prime = [False] * N
    
    
    def Eratosthenes(n):
        is_prime[0] = is_prime[1] = False
        for i in range(2, n + 1):
            is_prime[i] = True
        # neka i ide do <= sqrt(n)
        for i in range(2, isqrt(n) + 1):  # `isqrt` je funkcija dodana u Pythonu 3.8
            if is_prime[i]:
                for j in range(i * i, n + 1, i):
                    is_prime[j] = False
        for i in range(2, n + 1):
            if is_prime[i]:
                prime.append(i)
    ```

Ova optimizacija ne utječe na asimptotsku vremensku složenost; zapravo, ponavljanjem gornjeg dokaza dobivamo $n \ln \ln \sqrt n + o(n)$, što je prema svojstvima logaritma asimptotski jednako, ali se broj operacija znatno smanjuje.

#### Prosijavanje samo neparnih brojeva

Budući da su svi parni brojevi osim 2 složeni, možemo ih jednostavno preskočiti i baviti se samo neparnim brojevima.

Prvo, time prepolovljujemo potrebnu memoriju; drugo, i broj potrebnih operacija otprilike se prepolovljuje.

#### Smanjenje zauzeća memorije

Primijetimo da nam pri prosijavanju treba samo polje tipa `bool`. Jedan element polja `bool` obično zauzima $1$ bajt (tj. $8$ bitova), ali je za pohranu jedne logičke vrijednosti dovoljan $1$ bit.

Pomoću znanja o [bitovnim operacijama](../bit.md) svaku logičku vrijednost možemo spakirati u jedan bit; tako koristimo samo $n$ bitova (tj. $\dfrac n 8$ bajtova) umjesto $n$ bajtova, što znatno smanjuje zauzeće memorije. Taj se način naziva „pakiranje na razini bitova” (bit packing).

Vrijedi spomenuti da postoje strukture podataka koje automatski provode pakiranje na razini bitova, kao što su `vector<bool>` i `bitset<>` u C++-u.

Osim toga, `vector<bool>` i `bitset<>` donose programu poboljšanje konstante: Eratostenovo sito vremenske složenosti $O(n \log \log n)$ optimizirano pomoću `bitset<>` ili `vector<bool>` po brzini čak nadmašuje Eulerovo sito vremenske složenosti $O(n)$.

Vidi [bitset: kombinacija s Eratostenovim sitom](../../lang/csl/bitset.md#与埃氏筛结合).

#### Blokovsko prosijavanje

Iz optimizacije „prosijavanje do korijena” slijedi da nije potrebno stalno čuvati cijelo polje `is_prime[1...n]`. Za prosijavanje je dovoljno čuvati samo proste brojeve do $\sqrt n$, tj. `prime[1...sqrt(n)]`, a cijeli raspon podijeliti na blokove i svaki blok prosijati zasebno. Tako ne moramo istodobno držati više blokova u memoriji, a CPU bolje iskorištava priručnu memoriju (cache).

Neka je $s$ konstanta koja određuje veličinu bloka; tada imamo $\lceil {\frac n s} \rceil$ blokova, a blok $k$ ($k = 0 \dots \lfloor {\frac n s} \rfloor$) sadrži brojeve iz intervala $[ks, ks + s - 1]$. Blokove možemo obrađivati redom, tj. za svaki blok $k$ prolazimo kroz sve proste brojeve (od $1$ do $\sqrt n$) i njima prosijavamo.

Treba napomenuti da pri obradi prvog bloka strategiju treba malo prilagoditi: prvo, treba sačuvati sve proste brojeve iz $[1, \sqrt n]$; drugo, brojeve $0$ i $1$ treba označiti kao brojeve koji nisu prosti. Pri obradi posljednjeg bloka ne smije se zaboraviti da posljednji broj $n$ ne mora nužno biti na kraju bloka.

Sljedeća implementacija blokovskim prosijavanjem računa broj prostih brojeva manjih ili jednakih $n$.

???+ note "Implementacija"
    ```cpp
    int count_primes(int n) {
      constexpr static int S = 10000;
      vector<int> primes;
      int nsqrt = sqrt(n);
      vector<char> is_prime(nsqrt + 1, true);
      for (int i = 2; i <= nsqrt; i++) {
        if (is_prime[i]) {
          primes.push_back(i);
          for (int j = i * i; j <= nsqrt; j += i) is_prime[j] = false;
        }
      }
      int result = 0;
      vector<char> block(S);
      for (int k = 0; k * S <= n; k++) {
        fill(block.begin(), block.end(), true);
        int start = k * S;
        for (int p : primes) {
          int start_idx = (start + p - 1) / p;
          int j = max(start_idx, p) * p - start;
          for (; j < S; j += p) block[j] = false;
        }
        if (k == 0) block[0] = block[1] = false;
        for (int i = 0; i < S && start + i <= n; i++) {
          if (block[i]) result++;
        }
      }
      return result;
    }
    ```

Asimptotska vremenska složenost blokovskog sita jednaka je onoj Eratostenova sita (osim ako su blokovi vrlo mali), ali se potrebna memorija smanjuje na $O(\sqrt{n} + S)$ i bolje se iskorištava priručna memorija.
S druge strane, za svaki par bloka i prostog broja iz intervala $[1, \sqrt{n}]$ treba obaviti dijeljenje, što je za manje blokove znatno gore.
Zato pri odabiru konstante $S$ treba naći ravnotežu.

Najbolja brzina postiže se za veličinu bloka $S$ između $10^4$ i $10^5$.

### Linearno sito

Eratostenovo sito još ima prostora za optimizaciju: isti složeni broj označava više puta. Postoji li način da se uštede ti besmisleni koraci? Odgovor je potvrdan.

Ako postignemo da se svaki složeni broj označi točno jednom, vremenska se složenost može spustiti na $O(n)$.

???+ note "Implementacija"
    === "C++"
        ```cpp
        vector<int> pri;
        bool not_prime[N];
        
        void pre(int n) {
          for (int i = 2; i <= n; ++i) {
            if (!not_prime[i]) {
              pri.push_back(i);
            }
            for (int pri_j : pri) {
              if (i * pri_j > n) break;
              not_prime[i * pri_j] = true;
              if (i % pri_j == 0) {
                // i % pri_j == 0
                // drugim riječima, i je već prosijan brojem pri_j
                // budući da su prosti brojevi u pri poredani od manjeg prema većem,
                // umnožak i s drugim prostim brojevima sigurno će biti prosijan kao
                // višekratnik broja pri_j, pa ga ovdje ne treba prosijavati; zato
                // ovdje jednostavno prekidamo petlju (break)
                break;
              }
            }
          }
        }
        ```
    
    === "Python"
        ```python
        pri = []
        not_prime = [False] * N
        
        
        def pre(n):
            for i in range(2, n + 1):
                if not not_prime[i]:
                    pri.append(i)
                for pri_j in pri:
                    if i * pri_j > n:
                        break
                    not_prime[i * pri_j] = True
                    if i % pri_j == 0:
                        """
                        i % pri_j == 0
                        drugim riječima, i je već prosijan brojem pri_j
                        budući da su prosti brojevi u pri poredani od manjeg prema većem,
                        umnožak i s drugim prostim brojevima sigurno će biti prosijan kao
                        višekratnik broja pri_j, pa ga ovdje ne treba prosijavati; zato
                        ovdje jednostavno prekidamo petlju (break)
                        """
                        break
        ```

Gore opisano **linearno sito** naziva se i **Eulerovo sito**.

???+ note "Napomena"
    Primijetimo da pri traženju prostih brojeva sitom usput dobivamo i najmanji prosti faktor svakog broja.

## Sito za Eulerovu funkciju

Primijetimo da se u linearnom situ svaki složeni broj prosijava svojim najmanjim prostim faktorom. Na primjer, neka je $p_1$ najmanji prosti faktor broja $n$ i $n' = \frac{n}{p_1}$; tada se u linearnom situ $n$ prosijava kao $n' \times p_1$.

Promatrajući postupak linearnog sita, trebamo obraditi još dva dijela; u nastavku razlikujemo slučajeve prema $n' \bmod p_1$.

Ako je $n' \bmod p_1 = 0$, tada $n'$ sadrži sve proste faktore broja $n$.

$$
\begin{aligned}
\varphi(n) & = n \times \prod_{i = 1}^s{\frac{p_i - 1}{p_i}} \\\\
& = p_1 \times n' \times \prod_{i = 1}^s{\frac{p_i - 1}{p_i}} \\\\
& = p_1 \times \varphi(n')
\end{aligned}
$$

A što ako je $n' \bmod p_1 \neq 0$? Tada su $n'$ i $p_1$ relativno prosti, pa prema svojstvima Eulerove funkcije imamo:

$$
\begin{aligned}
\varphi(n) & = \varphi(p_1) \times \varphi(n') \\\\
& = (p_1 - 1) \times \varphi(n')
\end{aligned}
$$

### Implementacija

=== "C++"
    ```cpp
    vector<int> pri;
    bool not_prime[N];
    int phi[N];
    
    void pre(int n) {
      phi[1] = 1;
      for (int i = 2; i <= n; i++) {
        if (!not_prime[i]) {
          pri.push_back(i);
          phi[i] = i - 1;
        }
        for (int pri_j : pri) {
          if (i * pri_j > n) break;
          not_prime[i * pri_j] = true;
          if (i % pri_j == 0) {
            phi[i * pri_j] = phi[i] * pri_j;
            break;
          }
          phi[i * pri_j] = phi[i] * phi[pri_j];
        }
      }
    }
    ```

=== "Python"
    ```python
    pri = []
    not_prime = [False] * N
    phi = [0] * N
    
    
    def pre(n):
        phi[1] = 1
        for i in range(2, n + 1):
            if not not_prime[i]:
                pri.append(i)
                phi[i] = i - 1
            for pri_j in pri:
                if i * pri_j > n:
                    break
                not_prime[i * pri_j] = True
                if i % pri_j == 0:
                    phi[i * pri_j] = phi[i] * pri_j
                    break
                phi[i * pri_j] = phi[i] * phi[pri_j]
    ```

## Sito za Möbiusovu funkciju

### Definicija

Prema definiciji Möbiusove funkcije, neka je $n$ složen broj, $p_1$ najmanji prosti faktor broja $n$ i $n'=\frac{n}{p_1}$; tada vrijedi:

$$
\mu(n)=
\begin{cases}
    0 & n' \bmod p_1 = 0\\\\
    -\mu(n') & \text{otherwise}
\end{cases}
$$

Ako je $n$ prost, vrijedi $\mu(n)=-1$.

### Implementacija

=== "C++"
    ```cpp
    vector<int> pri;
    bool not_prime[N];
    int mu[N];
    
    void pre(int n) {
      mu[1] = 1;
      for (int i = 2; i <= n; ++i) {
        if (!not_prime[i]) {
          mu[i] = -1;
          pri.push_back(i);
        }
        for (int pri_j : pri) {
          if (i * pri_j > n) break;
          not_prime[i * pri_j] = true;
          if (i % pri_j == 0) {
            mu[i * pri_j] = 0;
            break;
          }
          mu[i * pri_j] = -mu[i];
        }
      }
    }
    ```

=== "Python"
    ```python
    pri = []
    not_prime = [False] * N
    mu = [0] * N
    
    
    def pre(n):
        mu[1] = 1
        for i in range(2, n + 1):
            if not not_prime[i]:
                pri.append(i)
                mu[i] = -1
            for pri_j in pri:
                if i * pri_j > n:
                    break
                not_prime[i * pri_j] = True
                if i % pri_j == 0:
                    mu[i * pri_j] = 0
                    break
                mu[i * pri_j] = -mu[i]
    ```

## Sito za broj djelitelja

Neka $d_i$ označava broj djelitelja broja $i$, a $num_i$ broj pojavljivanja najmanjeg prostog faktora broja $i$.

### Teorem o broju djelitelja

Teorem: ako je $n=\prod_{i=1}^m p_i^{c_i}$, tada je $d_i=\prod_{i=1}^m (c_i+1)$.

Dokaz: znamo da su djelitelji broja $p_i^{c_i}$ brojevi $p_i^0,p_i^1,\dots ,p_i^{c_i}$, ukupno njih $c_i+1$; prema principu produkta broj djelitelja broja $n$ jest $\prod_{i=1}^m (c_i+1)$.

### Implementacija

Budući da je $d_i$ multiplikativna funkcija, može se koristiti linearno sito.

Ovdje ukratko opisujemo načelo implementacije linearnim sitom.

1.  Kad je $i$ prost, $\textit{num}_i \gets 1,\textit{d}_i \gets 2$; ujedno neka je $q = \left\lfloor \dfrac {i}{p} \right\rfloor$, gdje je $p$ najmanji prosti faktor broja $i$.
2.  Kad je $p$ prosti faktor broja $q$, $\textit{num}_i \gets \textit{num}_q + 1,\textit{d}_i \gets \dfrac{\textit{d}_q}{\textit{num}_i} \times (\textit{num}_i + 1)$.
3.  Kad su $p,q$ relativno prosti, $\textit{num}_i \gets 1,\textit{d}_i \gets \textit{d}_q \times (\textit{num}_i+1)$.

=== "C++"
    ```cpp
    vector<int> pri;
    bool not_prime[N];
    int d[N], num[N];
    
    void pre(int n) {
      d[1] = 1;
      for (int i = 2; i <= n; ++i) {
        if (!not_prime[i]) {
          pri.push_back(i);
          d[i] = 2;
          num[i] = 1;
        }
        for (int pri_j : pri) {
          if (i * pri_j > n) break;
          not_prime[i * pri_j] = true;
          if (i % pri_j == 0) {
            num[i * pri_j] = num[i] + 1;
            d[i * pri_j] = d[i] / num[i * pri_j] * (num[i * pri_j] + 1);
            break;
          }
          num[i * pri_j] = 1;
          d[i * pri_j] = d[i] * 2;
        }
      }
    }
    ```

=== "Python"
    ```python
    pri = []
    not_prime = [False] * N
    d = [0] * N
    num = [0] * N
    
    
    def pre(n):
        d[1] = 1
        for i in range(2, n + 1):
            if not not_prime[i]:
                pri.append(i)
                d[i] = 2
                num[i] = 1
            for pri_j in pri:
                if i * pri_j > n:
                    break
                not_prime[i * pri_j] = True
                if i % pri_j == 0:
                    num[i * pri_j] = num[i] + 1
                    d[i * pri_j] = d[i] // num[i * pri_j] * (num[i * pri_j] + 1)
                    break
                num[i * pri_j] = 1
                d[i * pri_j] = d[i] * 2
    ```

## Sito za zbroj djelitelja

$f_i$ označava zbroj djelitelja broja $i$, a $g_i$ zbroj $p^0+p^1+p^2+\dots p^k$ za najmanji prosti faktor $p$ broja $i$.

### Implementacija

=== "C++"
    ```cpp
    vector<int> pri;
    bool not_prime[N];
    int g[N], f[N];
    
    void pre(int n) {
      g[1] = f[1] = 1;
      for (int i = 2; i <= n; ++i) {
        if (!not_prime[i]) {
          pri.push_back(i);
          g[i] = i + 1;
          f[i] = i + 1;
        }
        for (int pri_j : pri) {
          if (i * pri_j > n) break;
          not_prime[i * pri_j] = true;
          if (i % pri_j == 0) {
            g[i * pri_j] = g[i] * pri_j + 1;
            f[i * pri_j] = f[i] / g[i] * g[i * pri_j];
            break;
          }
          f[i * pri_j] = f[i] * f[pri_j];
          g[i * pri_j] = 1 + pri_j;
        }
      }
    }
    ```

=== "Python"
    ```python
    pri = []
    not_prime = [False] * N
    f = [0] * N
    g = [0] * N
    
    
    def pre(n):
        g[1] = f[1] = 1
        for i in range(2, n + 1):
            if not not_prime[i]:
                pri.append(i)
                g[i] = i + 1
                f[i] = i + 1
            for pri_j in pri:
                if i * pri_j > n:
                    break
                not_prime[i * pri_j] = True
                if i % pri_j == 0:
                    g[i * pri_j] = g[i] * pri_j + 1
                    f[i * pri_j] = f[i] // g[i] * g[i * pri_j]
                    break
                f[i * pri_j] = f[i] * f[pri_j]
                g[i * pri_j] = 1 + pri_j
    ```

## Opće multiplikativne funkcije

Ako [multiplikativna funkcija](./basic.md#multiplikativne-funkcije)  $f$ zadovoljava: za svaki prosti broj $p$ i prirodan broj $k$ vrijednost $f(p^k)$ može se izračunati u vremenu polinomnom niskog stupnja u $k$, tada se vrijednosti $f(1),f(2),\dots,f(n)$ mogu prosijati u vremenu $O(n)$.

Neka je rastav složenog broja $n$ na proste faktore $\prod_{i=1}^k p_i^{\alpha_i}$, gdje su $p_1<p_2<\dots<p_k$ prosti brojevi; u linearnom situ pamtimo $g_n=p_1^{\alpha_1}$. Ako se $n$ prosijava kao $x\cdot p$ ($p$ je prost), tada $g$ zadovoljava sljedeću rekurziju:

$$
g_n=
\begin{cases}
    g_x\cdot p & x\bmod p=0\\\\
    p & \text{otherwise}
\end{cases}
$$

Ako je $n=g_n$, to znači da je $n$ potencija nekog prostog broja i $f(n)$ se može izračunati u $O(1)$; inače je $f(n)=f(\frac{n}{g_n})\cdot f(g_n)$.

**Dio sadržaja ovog odjeljka preveden je iz blog-članka [Решето Эратосфена](http://e-maxx.ru/algo/eratosthenes_sieve) i njegova engleskog prijevoda [Sieve of Eratosthenes](https://cp-algorithms.com/algebra/sieve-of-eratosthenes.html). Ruska je inačica objavljena pod licencijom Public Domain + Leave a Link, a engleska pod licencijom CC-BY-SA 4.0.**
