---
title: Permutacije i kombinacije
---

## Uvod

Permutacije i kombinacije temelj su kombinatorike. Razmještaj (varijacija) znači da iz zadanog broja elemenata izaberemo zadani broj elemenata i poredamo ih; kombinacija znači da iz zadanog broja elemenata samo izaberemo zadani broj elemenata, ne obazirući se na poredak. Središnji problem permutacija i kombinacija jest proučavanje ukupnog broja mogućih razmještaja i kombinacija koji zadovoljavaju zadane uvjete. Permutacije i kombinacije usko su povezane s klasičnom teorijom vjerojatnosti.

U srednjoškolskoj elementarnoj matematici zadaci o permutacijama i kombinacijama uglavnom se rješavaju metodama poput tabličnog zapisa i nabrajanja.

## Princip zbroja i princip umnoška

### Princip zbroja

Ako se neki posao može obaviti na $n$ vrsta načina i $a_i(1 \le i \le n)$ označava broj načina $i$-te vrste, tada se taj posao može obaviti na ukupno $S=a_1+a_2+\cdots +a_n$ različitih načina.

### Princip umnoška

Ako se neki posao obavlja u $n$ koraka i $a_i(1 \le i \le n)$ označava broj različitih načina za $i$-ti korak, tada se taj posao može obaviti na ukupno $S = a_1 \times a_2 \times \cdots \times a_n$ različitih načina.

## Osnove varijacija i kombinacija

### Broj varijacija

Ako iz $n$ različitih elemenata izaberemo bilo kojih $m$ ($m\leq n$; $m$ i $n$ su prirodni brojevi, isto vrijedi i dalje u tekstu) elemenata i poredamo ih u niz određenim redoslijedom, to se naziva varijacija (razmještaj, engl. arrangement ili k-permutation) od $m$ elemenata izabranih među $n$ različitih elemenata; broj svih varijacija od $m$ ($m\leq n$) elemenata izabranih među $n$ različitih elemenata naziva se brojem varijacija od $m$ elemenata izabranih među $n$ različitih elemenata i označava se simbolom $\mathrm A_n^m$ (ili $\mathrm P_n^m$).

Formula za broj varijacija glasi:

$$
\mathrm A_n^m = n(n-1)(n-2) \cdots (n-m+1) = \frac{n!}{(n - m)!}
$$

$n!$ označava faktorijel broja $n$, npr. $6! = 1 \times 2 \times 3 \times 4 \times 5 \times 6$.

Formulu možemo shvatiti ovako: od $n$ osoba biramo $m$ koje će stati u red ($m \le n$). Za prvo mjesto možemo izabrati $n$ osoba, za drugo $n-1$, i tako dalje; za $m$-to (posljednje) mjesto možemo izabrati $n-m+1$ osoba, pa dobivamo:

$$
\mathrm A_n^m = n(n-1)(n-2) \cdots (n-m+1) = \frac{n!}{(n - m)!}
$$

Permutacija (potpuni razmještaj): svih $n$ osoba staje u red, duljina reda je $n$. Za prvo mjesto možemo izabrati $n$ osoba, za drugo $n-1$, i tako dalje, pa dobivamo:

$$
\mathrm A_n^n = n(n-1)(n-2) \cdots 3 \times 2 \times 1 = n!
$$

Permutacija je poseban slučaj varijacije.

### Broj kombinacija

Ako iz $n$ različitih elemenata izaberemo bilo kojih $m \leq n$ elemenata i od njih napravimo skup, to se naziva kombinacija od $m$ elemenata izabranih među $n$ različitih elemenata; broj svih kombinacija od $m \leq n$ elemenata izabranih među $n$ različitih elemenata naziva se brojem kombinacija od $m$ elemenata izabranih među $n$ različitih elemenata, označava se simbolom $\dbinom{n}{m}$ i čita se „$n$ povrh $m$”.

Formula za broj kombinacija:

$$
\dbinom{n}{m} = \frac{\mathrm A_n^m}{m!} = \frac{n!}{m!(n - m)!}
$$

Kako shvatiti gornju formulu? Promotrimo izbor $m$ od $n$ osoba ($m \le n$), bez postrojavanja u red, ne mareći za poredak. Kad bi nam poredak bio važan, dobili bismo $\mathrm A_n^m$; budući da nije, moramo ukloniti ponavljanja. Koliko se puta nešto ponavlja? Istih $m$ izabranih osoba može se još „potpuno razmjestiti” na $m!$ načina, pa dobivamo:

$$
\begin{aligned}
\dbinom{n}{m} \times m! &= \mathrm A_n^m\\
\dbinom{n}{m} &= \frac{\mathrm A_n^m}{m!} = \frac{n!}{m!(n-m)!}
\end{aligned}
$$

Broj kombinacija često se označava i s $\mathrm C_n^m$, tj. $\displaystyle \mathrm C_n^m=\binom{n}{m}$. U suvremenoj matematici općenito se koristi oznaka $\dbinom{n}{m}$, a ne $\mathrm C_n^m$.

Brojevi kombinacija nazivaju se i „binomnim koeficijentima”; vezu će objasniti binomni teorem u nastavku.

Posebno se dogovorno uzima da je za $m>n$ $\mathrm A_n^m=\dbinom{n}{m}=0$.

## Metoda pregrada

Metoda pregrada (stars and bars) tehnika je za određivanje broja načina da se jednaki elementi podijele u skupine, a može se koristiti i za određivanje broja rješenja jedne klase linearnih diofantskih jednadžbi.

### Broj rastava na zbroj pozitivnih cijelih brojeva

Problem 1: Imamo $n$ **potpuno jednakih** elemenata koje treba podijeliti u $k$ skupina tako da svaka skupina sadrži barem jedan element. Koliko ima načina podjele?

Zamislimo da $k - 1$ pregrada umećemo u $n - 1$ praznina između susjednih parova od $n$ elemenata.

Budući da su elementi potpuno jednaki, odgovor je upravo $\dbinom{n - 1}{k - 1}$.

U biti se traži broj rješenja jednadžbe $x_1+x_2+\cdots+x_k=n$ u pozitivnim cijelim brojevima.

### Broj rastava na zbroj nenegativnih cijelih brojeva

Problem 2: Što ako problem malo promijenimo pa dopustimo da skupine budu prazne?

Očito sada ne možemo izravno umetati pregrade, jer se može dogoditi da se više pregrada umetne u istu prazninu, što je vrlo nezgodno za računanje.

Pokušajmo stvoriti uvjete da se problem svede na ograničeni problem 1: prvo posudimo $k$ elemenata, pa u $n + k - 1$ praznina koje tvori tih $n + k$ elemenata umećemo pregrade; odgovor je

$$
\binom{n + k - 1}{k - 1} = \binom{n + k - 1}{n}
$$

Iako nismo izravno riješili izvorni problem, taj je izraz upravo odgovor na izvorni problem, što se može shvatiti ovako:

Na početku smo posudili $k$ elemenata kako bismo osigurali da svaka skupina sadrži barem jedan element; nakon umetanja pregrada tih $k$ posuđenih elemenata uzmemo natrag iz $k$ skupina. Budući da su elementi jednaki, situacije nakon transformacije i prije nje međusobno su u bijekciji, pa su i odgovori jednaki.

Odatle slijedi formula metode pregrada: $\dbinom{n + k - 1}{n}$.

U biti se traži broj rješenja jednadžbe $x_1+x_2+\cdots+x_k=n$ u nenegativnim cijelim brojevima (tj. zahtijeva se $x_i \ge 0$).

### Broj rastava na zbroj cijelih brojeva s različitim donjim ogradama

Problem 3: Što ako problem proširimo još jedan korak i zahtijevamo da $i$-ta skupina dobije barem $a_i,\sum a_i \le n$ elemenata?

U biti se traži broj rješenja jednadžbe $x_1+x_2+\cdots+x_k=n$ u kojima je $x_i \ge a_i$.

Analogno slučaju bez ograničenja, posudimo $\sum a_i$ elemenata kako bismo osigurali da $i$-ta skupina dobije barem $a_i$ elemenata. Drugim riječima, stavimo

$$
x_i^{\prime}=x_i-a_i
$$

i dobivamo novu jednadžbu:

$$
\begin{aligned}
(x_1^{\prime}+a_1)+(x_2^{\prime}+a_2)+\cdots+(x_k^{\prime}+a_k)&=n\\
x_1^{\prime}+x_2^{\prime}+\cdots+x_k^{\prime}&=n-a_1-a_2-\cdots-a_k\\
x_1^{\prime}+x_2^{\prime}+\cdots+x_k^{\prime}&=n-\sum a_i
\end{aligned}
$$

pri čemu je

$$
x_i^{\prime}\ge 0
$$

Time se problem 3 sveo na problem 2, pa izravno iz formule metode pregrada dobivamo odgovor

$$
\binom{n - \sum a_i + k - 1}{n - \sum a_i}
$$

### Nesusjedni razmještaji

Ako među $n$ prirodnih brojeva $1 \sim n$ biramo $k$ brojeva tako da nikoja dva od tih $k$ brojeva nisu susjedna, broj takvih kombinacija je $\dbinom {n-k+1}{k}$.

## Binomni teorem

Prije nego što prijeđemo na napredni dio o permutacijama i kombinacijama, predstavimo teorem usko povezan s binomnim koeficijentima – binomni teorem.

Binomni teorem opisuje koeficijente razvoja:

$$
(a+b)^n=\sum_{i=0}^n\binom{n}{i}a^{n-i}b^i
$$

Dokaz se može provesti matematičkom indukcijom, koristeći $\dbinom{n}{k}+\dbinom{n}{k-1}=\dbinom{n+1}{k}$ u koraku indukcije.

Binomni teorem lako se poopćuje i na polinomni (multinomni) oblik:

Neka je $n$ pozitivan cijeli broj, a $x_i$ realni brojevi; tada je

$$
(x_1 + x_2 + \cdots + x_t)^n = \sum_{\text{nenegativna cjelobrojna rješenja od } n_1 + \cdots + n_t=n} \binom{n}{n_1,n_2,\cdots,n_t} x_1^{n_1}x_2^{n_2}\cdots x_t^{n_t}
$$

pri čemu je $\dbinom{n}{n_1,n_2,\cdots,n_t}$ multinomni koeficijent, čija su svojstva također vrlo slična:

$$
\sum{\binom{n}{n_1,n_2,\cdots,n_t}} = t^n
$$

## Napredne permutacije i kombinacije

U nastavku predstavljamo neke varijante permutacija i kombinacija.

### Broj permutacija multiskupa | multinomni koeficijent

Obavezno razlikujte **multinomni koeficijent** od **broja kombinacija multiskupa**! To su dva potpuno različita pojma!

Multiskup je poopćeni skup koji može sadržavati ponovljene elemente. Neka $S=\{n_1\cdot a_1,n_2\cdot a_2,\cdots,n_k\cdot a_k\}$ označava multiskup sastavljen od $n_1$ elemenata $a_1$, $n_2$ elemenata $a_2$, …, $n_k$ elemenata $a_k$; broj permutacija multiskupa $S$ jednak je

$$
\frac{n!}{\prod_{i=1}^kn_i!}=\frac{n!}{n_1!n_2!\cdots n_k!}
$$

To odgovara tome da se podijeli brojem razmještaja jednakih elemenata. Konkretno, možete zamisliti da imate $k$ vrsta različitih kuglica, pri čemu je broj kuglica svake vrste redom $n_1,n_2,\cdots,n_k$ i $n=n_1+n_2+\ldots+n_k$. Broj permutacija tih $n$ kuglica upravo je **broj permutacija multiskupa**. Broj permutacija multiskupa često se naziva **multinomnim koeficijentom**. Gornji izraz možemo zapisati simbolom multinomnog koeficijenta:

$$
\binom{n}{n_1,n_2,\cdots,n_k}=\frac{n!}{\prod_{i=1}^kn_i!}
$$

Vidi se da je $\dbinom{n}{m}$ ekvivalentno $\dbinom{n}{m,n-m}$, samo što je potonji zapis glomazniji pa se ne koristi.

### Broj kombinacija multiskupa 1

Neka $S=\{n_1\cdot a_1,n_2\cdot a_2,\cdots,n_k\cdot a_k\}$ označava multiskup sastavljen od $n_1$ elemenata $a_1$, $n_2$ elemenata $a_2$, …, $n_k$ elemenata $a_k$. Tada je za cijeli broj $r(r<n_i,\forall i\in[1,k])$ broj načina da iz $S$ izaberemo $r$ elemenata koji tvore multiskup upravo **broj kombinacija multiskupa**. Taj je problem ekvivalentan broju rješenja jednadžbe $x_1+x_2+\cdots+x_k=r$ u nenegativnim cijelim brojevima, može se riješiti metodom pregrada, a odgovor je

$$
\binom{r+k-1}{k-1}
$$

### Broj kombinacija multiskupa 2

Razmotrimo sljedeći problem: neka $S=\{n_1\cdot a_1,n_2\cdot a_2,\cdots,n_k\cdot a_k,\}$ označava multiskup sastavljen od $n_1$ elemenata $a_1$, $n_2$ elemenata $a_2$, …, $n_k$ elemenata $a_k$. Tražimo, za pozitivan cijeli broj $r$, broj načina da iz $S$ izaberemo $r$ elemenata koji tvore multiskup.

Sada je broj uzetih elemenata svake vrste ograničen. Jednako kao prije, problem možemo pretvoriti u rješavanje linearne jednadžbe s ograničenjima:

$$
\forall i\in [1,k],\ x_i\le n_i,\ \sum_{i=1}^kx_i=r
$$

Prirodno se nameće formula uključivanja-isključivanja. Model uključivanja-isključivanja je sljedeći:

1.  Univerzalni skup: nenegativna cjelobrojna rješenja jednadžbe $\displaystyle \sum_{i=1}^kx_i=r$.
2.  Svojstva: $x_i\le n_i$.

Neka je $S_i$ skup rješenja koja zadovoljavaju svojstvo $i$, a $\overline{S_i}$ skup onih koja ne zadovoljavaju svojstvo $i$, tj. skup rješenja s $x_i\ge n_i+1$ (što se svodi na problem 3 metode pregrada). Tada je odgovor

$$
\left|\bigcap_{i=1}^kS_i\right|=|U|-\left|\bigcup_{i=1}^k\overline{S_i}\right|
$$

Prema formuli uključivanja-isključivanja vrijedi:

$$
\begin{aligned}
\left|\bigcup_{i=1}^k\overline{S_i}\right|
=&\sum_i\left|\overline{S_i}\right|
-\sum_{i,j}\left|\overline{S_i}\cap\overline{S_j}\right|
+\sum_{i,j,k}\left|\overline{S_i}\cap\overline{S_j}\cap\overline{S_k}\right|
-\cdots\\
&+(-1)^{k-1}\left|\bigcap_{i=1}^k\overline{S_i}\right|\\
=&\sum_i\binom{k+r-n_i-2}{k-1}
-\sum_{i,j}\binom{k+r-n_i-n_j-3}{k-1}+\sum_{i,j,k}\binom{k+r-n_i-n_j-n_k-4}{k-1}
-\cdots\\
&+(-1)^{k-1}\binom{k+r-\sum_{i=1}^kn_i-k-1}{k-1}
\end{aligned}
$$

Oduzimanjem gornjeg izraza od univerzalnog skupa $\displaystyle |U|=\binom{k+r-1}{k-1}$ dobivamo broj kombinacija multiskupa

$$
Ans=\sum_{p=0}^k(-1)^p\sum_{A}\binom{k+r-1-\sum_{A} n_{A_i}-p}{k-1}
$$

pri čemu A služi za nabrajanje podskupova i zadovoljava $|A|=p,\ A_i<A_{i+1}$.

### Kružni razmještaji

Svih $n$ osoba stane u krug; broj svih takvih razmještaja označimo s $\mathrm Q_n^n$. Promotrimo jedan već složen krug: ako ga prekinemo na različitim mjestima, dobivamo različite redove.
Stoga vrijedi

$$
\mathrm Q_n^n \times n = \mathrm A_n^n \Longrightarrow \mathrm Q_n = \frac{\mathrm A_n^n}{n} = (n-1)!
$$

Odatle slijedi formula za djelomične kružne razmještaje:

$$
\mathrm Q_n^r = \frac{\mathrm A_n^r}{r} = \frac{n!}{r \times (n-r)!}
$$

## Svojstva binomnih koeficijenata | posljedice binomnog teorema

Budući da su binomni koeficijenti vrlo važni u natjecateljskom programiranju (OI), ovdje predstavljamo neka njihova svojstva.

$$
\binom{n}{m}=\binom{n}{n-m}\tag{1}
$$

Odgovara tome da izabrani skup zamijenimo njegovim komplementom u odnosu na univerzalni skup, pa se vrijednost ne mijenja. (Simetričnost.)

$$
\binom{n}{k} = \frac{n}{k} \binom{n-1}{k-1}\tag{2}
$$

Rekurzivna formula izvedena iz definicije.

$$
\binom{n}{m}=\binom{n-1}{m}+\binom{n-1}{m-1}\tag{3}
$$

Rekurzivna formula za binomne koeficijente (formula Pascalova trokuta, u Kini poznatog kao Yang Huijev trokut). Pomoću nje možemo izračunati binomne koeficijente u složenosti $O(n^2)$.

$$
\binom{n}{0}+\binom{n}{1}+\cdots+\binom{n}{n}=\sum_{i=0}^n\binom{n}{i}=2^n\tag{4}
$$

To je poseban slučaj binomnog teorema. Uzmemo li $a=b=1$, dobivamo gornju formulu.

$$
\sum_{i=0}^n(-1)^i\binom{n}{i}=[n=0]\tag{5}
$$

Još jedan poseban slučaj binomnog teorema; uzmemo $a=1, b=-1$. Poseban slučaj ove formule je $n=0$, kada je rezultat $1$.

$$
\sum_{i=0}^k \binom{n}{i}\binom{m}{k-i} = \binom{m+n}{k}\tag{6}
$$

Formula za rastavljanje binomnih koeficijenata; koristi se pri rješavanju nekih zadataka sa strukturama podataka. Naziva se [Vandermondeovim identitetom](https://en.wikipedia.org/wiki/Vandermonde%27s_identity).

$$
\sum_{i=0}^n\binom{n}{i}^2=\binom{2n}{n}\tag{7}
$$

To je poseban slučaj formule $(6)$; dovoljno je uzeti $n=k=m$.

$$
\sum_{i=0}^ni\binom{n}{i}=n2^{n-1}\tag{8}
$$

Formula za težinsku sumu; može se dokazati deriviranjem polinomne funkcije koja odgovara formuli $(4)$.

$$
\sum_{i=0}^ni^2\binom{n}{i}=n(n+1)2^{n-2}\tag{9}
$$

Slično prethodnoj formuli, može se dokazati deriviranjem polinomne funkcije.

$$
\sum_{l=0}^n\binom{l}{k} = \binom{n+1}{k+1}\tag{10}
$$

Može se dokazati kombinatornom analizom, razmatrajući jedan po jedan $k+1$-člane podskupove skupa $S=\{a_1, a_2, \cdots, a_{n+1}\}$; često se koristi u dokazima identiteta. Naziva se [identitetom hokejaške palice (Zhu Shijieov identitet)](https://en.wikipedia.org/wiki/Hockey-stick_identity).

$$
\binom{n}{r}\binom{r}{k} = \binom{n}{k}\binom{n-k}{r-k}\tag{11}
$$

Može se dokazati iz definicije.

$$
\sum_{i=0}^n\binom{n-i}{i}=F_{n+1}\tag{12}
$$

pri čemu je $F$ Fibonaccijev niz.

$$
\binom{n+k}{k}^2=\sum_{j=0}^k\binom{k}{j}^2\binom{n+2k-j}{2k}\tag{13}
$$

Može se dokazati pomoću $(6)$. Naziva se [Li Shanlanovim identitetom](https://en.wikipedia.org/wiki/Li_Shanlan_identity).

## Binomna inverzija

Neka $f_n$ označava broj načina da se od točno $n$ različitih elemenata oblikuje određena struktura, a $g_n$ ukupan broj načina da se među $n$ različitih elemenata izabere $i \geq 0$ elemenata i od njih oblikuje određena struktura.

Ako je poznat $f_n$ i tražimo $g_n$, očito vrijedi:

$$
g_n = \sum_{i = 0}^{n} \binom{n}{i} f_i
$$

Ako je poznat $g_n$ i tražimo $f_n$, tada je:

$$
f_n = \sum_{i = 0}^{n} \binom{n}{i} (-1)^{n-i} g_i
$$

Opisani postupak određivanja $f_n$ iz poznatog $g_n$ naziva se **binomna inverzija**.

### Dokaz

Raspišemo li $g_i$ u formuli inverzije, dobivamo:

$$
\begin{aligned}
f_n &= \sum_{i = 0}^{n} \binom{n}{i} (-1)^{n-i} \left[\sum_{j = 0}^{i} \binom{i}{j} f_j\right] \\
&= \sum_{i = 0}^{n}\sum_{j = 0}^{i}\binom{n}{i}\binom{i}{j} (-1)^{n-i}f_j
\end{aligned}
$$

Prvo prolazimo po $j$, a zatim po $i$, pa dobivamo:

$$
\begin{aligned}
f_n &= \sum_{j = 0}^{n}\sum_{i = j}^{n}\binom{n}{i}\binom{i}{j} (-1)^{n-i}f_j \\
&= \sum_{j = 0}^{n}f_j\sum_{i = j}^{n}\binom{n}{i}\binom{i}{j} (-1)^{n-i}
\end{aligned}
$$

Primjenom formule (11) iz odjeljka [„Svojstva binomnih koeficijenata | posljedice binomnog teorema”](#svojstva-binomnih-koeficijenata--posljedice-binomnog-teorema) dobivamo:

$$
\begin{aligned}
f_n &= \sum_{j = 0}^{n}f_j\sum_{i = j}^{n}\binom{n}{j}\binom{n - j}{i - j} (-1)^{n-i} \\
&= \sum_{j = 0}^{n}\binom{n}{j}f_j\sum_{i = j}^{n}\binom{n - j}{i - j} (-1)^{n-i}
\end{aligned}
$$

Stavimo $k = i - j$. Tada je $i = k + j$, pa gornji izraz prelazi u:

$$
f_n = \sum_{j = 0}^{n}\binom{n}{j}f_j\sum_{k = 0}^{n - j}\binom{n - j}{k} (-1)^{n-j-k}1^{k}
$$

Primjenom formule (5) iz odjeljka [„Svojstva binomnih koeficijenata | posljedice binomnog teorema”](#svojstva-binomnih-koeficijenata--posljedice-binomnog-teorema) dobivamo:

$$
f_n = \sum_{j = 0}^{n}\binom{n}{j}f_j[n = j] = f_n
$$

Time je dokaz završen.
