---
title: Main–Lorentzov algoritam
---

## Tandemska ponavljanja

### Definicija

Zadana je duljina $n$ i string $s$ te duljine.

String dobiven zapisivanjem nekog stringa dvaput uzastopno zovemo **tandemskim ponavljanjem (tandem repetition)**. Radi preciznosti string koji se ponavlja u nastavku zovemo osnovnim stringom. Drugim riječima, tandemsko ponavljanje odgovara paru indeksa $(i, j)$ za koji je $s[i \dots j]$ spoj dvaju jednakih stringova.

Cilj je pronaći sva tandemska ponavljanja u zadanom stringu $s$. Možemo rješavati i jednostavniji problem: pronaći bilo koje tandemsko ponavljanje u stringu $s$ ili najdulje takvo ponavljanje.

Sljedeći algoritam predložili su Michael Main i Richard J. Lorentz 1982. godine.

???+ note "Dogovori"
    Svi indeksi stringova u nastavku počinju od $0$.
    
    Oznaka $\overline{s}$ predstavlja obrnuti string stringa $s$. Primjerice, $\overline{\tt abc} = \tt cba$.

### Objašnjenje

Promotrimo string $\tt acababaee$. Sadrži tri tandemska ponavljanja:

-   $s[2 \dots 5] = \tt abab$
-   $s[3 \dots 6] = \tt baba$
-   $s[7 \dots 8] = \tt ee$

Kao drugi primjer, string $\tt abaaba$ sadrži samo dva tandemska ponavljanja:

-   $s[0 \dots 5] = \tt abaaba$
-   $s[2 \dots 3] = \tt aa$

### Broj tandemskih ponavljanja

String duljine $n$ može sadržavati čak $O(n^2)$ tandemskih ponavljanja. Očit je primjer string od $n$ jednakih slova: svaki podstring parne duljine tandemsko je ponavljanje. Općenito, periodički string s kratkim periodom ima mnogo tandemskih ponavljanja.

Unatoč tome tandemska ponavljanja možemo prebrojiti u vremenu $O(n \log n)$ jer algoritam koristi sažeti prikaz koji više ponavljanja objedinjuje u jedan zapis.

Slijedi nekoliko zanimljivih činjenica o broju tandemskih ponavljanja:

-   Tandemsko ponavljanje čiji osnovni string nije tandemsko ponavljanje zovemo **primitivnim ponavljanjem (primitive repetition)**. Može se dokazati da primitivnih ponavljanja ima najviše $O(n \log n)$.
-   Tandemsko ponavljanje možemo sažeti Crochemoreovom trojkom $(i, p, r)$, gdje je $i$ početna pozicija, $p$ duljina jednog periodičkog bloka (ne nužno osnovnog stringa!), a $r$ broj ponavljanja tog bloka. Sva tandemska ponavljanja stringa tada se mogu prikazati s $O(n \log n)$ Crochemoreovih trojki.
-   Fibonaccijevi stringovi definirani su ovako:

$$
\begin{align} t_0 &= a, \\ t_1 &= b, \\ t_i &= t_{i-1} + t_{i-2}, \end{align}
$$

Fibonaccijevi stringovi izrazito su periodički. Za duljinu $f_i$ i Fibonaccijev string $t_i$ te duljine i nakon sažimanja Crochemoreovim trojkama ostaje $O(f_i \log f_i)$ trojki. Broj njegovih primitivnih ponavljanja također je $O(f_i \log f_i)$.

## Main–Lorentzov algoritam

### Objašnjenje

Osnovna je ideja Main–Lorentzova algoritma **divide and conquer**.

String dijelimo na lijevi i desni dio. Najprije brojimo tandemska ponavljanja potpuno sadržana u lijevom ili desnom dijelu, a zatim ona koja počinju u lijevom i završavaju u desnom dijelu. Takva ponavljanja u nastavku zovemo **prelazećim ponavljanjima**.

Brojanje prelazećih ponavljanja ključno je za Main–Lorentzov algoritam i detaljno ga razmatramo u nastavku.

### Postupak

#### Pronalaženje prelazećih ponavljanja

Lijevi dio označimo s $u$, a desni s $v$. Tada je $s = u + v$, a duljine $u, v$ približno su jednake polovini duljine stringa $s$.

Promotrimo srednji znak tandemskog ponavljanja, koji ovdje definiramo kao prvi znak njegove desne polovine. Drugim riječima, ako je $s[i...j]$ tandemsko ponavljanje, njegov je srednji znak $s[(i + j + 1)/2]$. Ponavljanje zovemo **lijevim (left)** ako se srednji znak nalazi u $u$, a inače **desnim (right)**.

U nastavku razmatramo kako pronaći sva lijeva ponavljanja.

Neka je duljina lijevog ponavljanja $2l$. Promotrimo njegov prvi znak u $v$, odnosno $s[|u|]$. U $u$ mora postojati jednak znak $u[\textit{cntr}]$.

Fiksiramo $\textit{cntr}$ i tražimo sva odgovarajuća ponavljanja. Primjerice, u stringu $\tt c \; \underset{\textit{cntr}}{a} \; c \; | \; a \; d \; a$ (gdje $\tt |$ razdvaja lijevi i desni dio) za fiksni $cntr = 1$ dobivamo ponavljanje $\tt caca$.

Fiksiranjem $\textit{cntr}$ očito fiksiramo i $l$. Kad znamo pronaći sva ponavljanja za fiksnu vrijednost, možemo od $0$ do $|u| - 1$ isprobati sve vrijednosti $\textit{cntr}$ i pronaći sva odgovarajuća ponavljanja.

#### Prepoznavanje lijevih ponavljanja

Čak i uz fiksni $\textit{cntr}$ više ponavljanja može zadovoljavati uvjete. Kako ih sve pronaći?

Promotrimo još jedan primjer: u stringu $\tt abcabcac$ nalazi se ponavljanje $\overbrace{\tt a}^{l_1} \overbrace{\underset{\textit{cntr}}{\tt b} \tt c}^{l_2} \overbrace{\tt a}^{l_1}  \; | \; \overbrace{\tt b \; \tt c}^{l_2}$. Neka je $l_1$ duljina od prvog znaka ponavljanja do $s[\textit{cntr} - 1]$, a $l_2$ duljina od $s[\textit{cntr}]$ do posljednjeg znaka lijevog osnovnog stringa ponavljanja.

Sada možemo navesti **nužan i dovoljan uvjet** da podstring duljine $2l = 2(l_1 + l_2) = 2(|u| - \textit{cntr})$ bude tandemsko ponavljanje:

Neka je $k_1$ najveći cijeli broj za koji vrijedi $u[\textit{cntr} - k_1 \dots \textit{cntr} - 1] = u[|u| - k_1 \dots |u| - 1]$, a $k_2$ najveći cijeli broj za koji vrijedi $u[\textit{cntr} \dots \textit{cntr} + k_2 - 1] = v[0 \dots k_2 - 1]$. Uz uvjete $l_1 \leq k_1$ i $l_2 \leq k_2$, svakom paru $(l_1, l_2)$ tada odgovara točno jedno tandemsko ponavljanje.

Ukratko:

-   Fiksiramo $\textit{cntr}$.
-   Sva tražena ponavljanja imaju duljinu $2l = 2(|u| - \textit{cntr})$. I dalje ih može biti više, ovisno o $l_1$ i $l_2$.
-   Izračunamo prethodno definirane $k_1$ i $k_2$.
-   Sva odgovarajuća ponavljanja zadovoljavaju:

$$
\begin{align} l_1 + l_2 &= l = |u| - \textit{cntr} \\ l_1 &\le k_1, \\ l_2 &\le k_2. \\ \end{align}
$$

Preostaje učinkovito izračunati $k_1$ i $k_2$. Pomoću [Z-funkcije](./z-func.md) možemo ih dobiti u vremenu $O(1)$:

-   Za $k_1$ izračunamo Z-funkciju stringa $\overline{u}$.
-   Za $k_2$ izračunamo Z-funkciju stringa $v + \# + u$, gdje je $\#$ znak koji se ne pojavljuje ni u $u$ ni u $v$.

#### Desna ponavljanja

Pronalaženje desnih ponavljanja gotovo je jednako pronalaženju lijevih. Promotrimo znak na granici u $u$, odnosno $s[|u| - 1]$. On mora biti jednak nekom znaku u $v$; poziciju tog znaka u $v$ označimo s $\textit{cntr}$.

Neka je $k_1$ najveći cijeli broj za koji vrijedi $v[\textit{cntr} - k_1 + 1 \dots \textit{cntr}] = u[|u| - k_1 \dots |u| - 1]$, a $k_2$ najveći cijeli broj za koji vrijedi $v[\textit{cntr} + 1 \dots \textit{cntr} + k_2] = v[0 \dots k_2 - 1]$. Računanjem Z-funkcija za $\overline{u} + \# + \overline{v}$ i $v$ dobivamo redom $k_1$ i $k_2$.

Isprobamo sve vrijednosti $\textit{cntr}$ i analognim postupkom pronađemo desna ponavljanja.

### Implementacija

Main–Lorentzov algoritam opisuje sva tandemska ponavljanja četvorkama $(\textit{cntr}, l, k_1, k_2)$. Ako samo želimo prebrojiti ponavljanja ili pronaći najdulje, te četvorke sadrže dovoljno podataka. Prema [glavnom teoremu](../basic/complexity.md#glavni-teorem), vremenska složenost iznosi $O(n \log n)$.

Primijetite da određivanje početne i završne pozicije svakog ponavljanja iz tih četvorki u najgorem slučaju traje $O(n^2)$. Sljedeća implementacija to radi i pohranjuje krajnje pozicije svih ponavljanja u `repetitions`.

```cpp
vector<int> z_function(string const& s) {
  int n = s.size();
  vector<int> z(n);
  for (int i = 1, l = 0, r = 0; i < n; i++) {
    if (i <= r) z[i] = min(r - i + 1, z[i - l]);
    while (i + z[i] < n && s[z[i]] == s[i + z[i]]) z[i]++;
    if (i + z[i] - 1 > r) {
      l = i;
      r = i + z[i] - 1;
    }
  }
  return z;
}

int get_z(vector<int> const& z, int i) {
  if (0 <= i && i < (int)z.size())
    return z[i];
  else
    return 0;
}

vector<pair<int, int>> repetitions;

void convert_to_repetitions(int shift, bool left, int cntr, int l, int k1,
                            int k2) {
  for (int l1 = max(1, l - k2); l1 <= min(l, k1); l1++) {
    if (left && l1 == l) break;
    int l2 = l - l1;
    int pos = shift + (left ? cntr - l1 : cntr - l - l1 + 1);
    repetitions.emplace_back(pos, pos + 2 * l - 1);
  }
}

void find_repetitions(string s, int shift = 0) {
  int n = s.size();
  if (n == 1) return;

  int nu = n / 2;
  int nv = n - nu;
  string u = s.substr(0, nu);
  string v = s.substr(nu);
  string ru(u.rbegin(), u.rend());
  string rv(v.rbegin(), v.rend());

  find_repetitions(u, shift);
  find_repetitions(v, shift + nu);

  vector<int> z1 = z_function(ru);
  vector<int> z2 = z_function(v + '#' + u);
  vector<int> z3 = z_function(ru + '#' + rv);
  vector<int> z4 = z_function(v);

  for (int cntr = 0; cntr < n; cntr++) {
    int l, k1, k2;
    if (cntr < nu) {
      l = nu - cntr;
      k1 = get_z(z1, nu - cntr);
      k2 = get_z(z2, nv + 1 + cntr);
    } else {
      l = cntr - nu + 1;
      k1 = get_z(z3, nu + 1 + nv - 1 - (cntr - nu));
      k2 = get_z(z4, (cntr - nu) + 1);
    }
    if (k1 + k2 >= l) convert_to_repetitions(shift, cntr < nu, cntr, l, k1, k2);
  }
}
```

**Ova je stranica uglavnom prevedena iz objave [Поиск всех тандемных повторов в строке. Алгоритм Мейна-Лоренца](http://e-maxx.ru/algo/string_tandems) i njezina engleskog prijevoda [Finding repetitions](https://cp-algorithms.com/string/main_lorentz.html). Ruska je inačica objavljena pod licencom Public Domain + Leave a Link, a engleska pod licencom CC-BY-SA 4.0.**
