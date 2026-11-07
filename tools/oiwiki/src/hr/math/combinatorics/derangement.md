---
title: Deranžmani
---

## Deranžmani

### Definicija

Deranžman (derangement) je permutacija u kojoj se nijedan element ne nalazi na svojem prirodnom mjestu. Drugim riječima, za permutaciju $P$ brojeva $1\sim n$ kažemo da je $P$ deranžman od $n$ ako vrijedi $P_i\neq i$.

Na primjer, deranžmani tri elementa su $\{2,3,1\}$ i $\{3,1,2\}$. Deranžmani četiri elementa su $\{2,1,4,3\}$, $\{2,3,4,1\}$, $\{2,4,1,3\}$, $\{3,1,4,2\}$, $\{3,4,1,2\}$, $\{3,4,2,1\}$, $\{4,1,2,3\}$, $\{4,3,1,2\}$ i $\{4,3,2,1\}$. Deranžman je permutacija bez fiksnih točaka, tj. bez ciklusa duljine 1.

### Računanje formulom uključivanja-isključivanja

Univerzalni skup $U$ skup je svih permutacija brojeva $1\sim n$, $|U|=n!$; neka je $S_i$ skup onih permutacija koje zadovoljavaju $P_i\neq i$. Primjenom komplementa i [formule uključivanja-isključivanja](./inclusion-exclusion-principle.md) problem se svodi na računanje:

$$
\begin{aligned}
\left|\bigcap_{i=1}^n S_i\right|
&=|U|-\left|\bigcup_{i=1}^n\overline{S_i}\right|\\
&=n!-\sum_{k=1}^n(-1)^{k-1}\sum_{a_i<a_{i+1}}\left|\bigcap_{i=1}^{k}\overline{S_{a_i}}\right|
\end{aligned}
$$

Pritom suma znači da iz $1, 2, \cdots, n$ biramo $a_1, a_2, \cdots, a_k$ tako da vrijedi $a_i<a_{i+1}$. Tada

$$
\left|\bigcap_{i=1}^{k}\overline{S_{a_i}}\right|
$$

označava broj permutacija u kojima $k$ brojeva $a_1,a_2,\cdots,a_k$ zadovoljava $P_{a_i}=a_i$, a položaji preostalih $n-k$ brojeva su proizvoljni, pa je:

$$
\left|\bigcap_{i=1}^{k}\overline{S_{a_i}}\right|=(n-k)!
$$

Tih $k$ brojeva može se odabrati na $\dbinom{n}{k}$ načina, pa zbrajanjem dobivamo:

$$
\begin{aligned}
&\sum_{k=1}^n(-1)^{k-1}\sum_{a_i<a_{i+1}}\left|\bigcap_{i=1}^{k}\overline{S_{a_i}}\right|\\
=&\sum_{k=1}^n(-1)^{k-1}\dbinom{n}{k}(n-k)!\\
=&\sum_{k=1}^n(-1)^{k-1}\frac{n!}{k!}\\
=&n!\sum_{k=1}^n\frac{(-1)^{k-1} }{k!}
\end{aligned}
$$

Stoga je broj deranžmana $n$ elemenata:

$$
D_n=n!-n!\sum_{k=1}^n\frac{(-1)^{k-1} }{k!}=n!\sum_{k=0}^n\frac{(-1)^k}{k!}
$$

Prvih nekoliko članova niza brojeva deranžmana su $0,1,2,9,44,265$ ([OEIS A000166](http://oeis.org/A000166)).

### Računanje rekurzijom

Konkretizirajmo problem deranžmana i razmotrimo sljedeći zadatak:

Imamo $n$ različitih pisama, označenih brojevima $1,2,3,4,5$, i tih pet pisama treba staviti u omotnice označene brojevima $1,2,3,4,5$ tako da se oznaka omotnice razlikuje od oznake pisma. Na koliko se različitih načina pisma mogu rasporediti?

Pretpostavimo da smo došli do $n$-te omotnice; na početku privremeno stavimo $n$-to pismo u $n$-tu omotnicu, a zatim razmotrimo rekurziju u dva slučaja:

-   prvih $n-1$ omotnica sve su krivo popunjene;
-   među prvih $n-1$ omotnica točno je jedna ispravno popunjena, a sve ostale krivo.

U prvom slučaju, kad su prvih $n-1$ omotnica sve krivo popunjene: budući da su prvih $n-1$ već sve krive, dovoljno je $n$-to pismo zamijeniti s bilo kojim od prethodnih položaja, što ukupno daje $D_{n-1}\times (n-1)$ mogućnosti.

U drugom slučaju, kad je među prvih $n-1$ omotnica točno jedna ispravna, a ostale krive: smisao razmatranja ovog slučaja jest u tome da, ako je među $n-1$ omotnica jedna ispravno popunjena, zamjenom te ispravne s $n$-tom dobivamo deranžman.

Iz ostalih slučajeva nije moguće jednom operacijom dobiti deranžman duljine $n$.

Odatle slijedi da brojevi deranžmana zadovoljavaju rekurzivnu relaciju:

$$
D_n=(n-1)(D_{n-1}+D_{n-2})
$$

Navedimo ovdje i drugu rekurzivnu relaciju:

$$
D_n=nD_{n-1}+{(-1)}^n
$$

### Ostale relacije

Broj deranžmana ima jednostavan izraz sa zaokruživanjem, a od faktorijela se po brzini rasta razlikuje samo za konstantu:

$$
D_n=\left\lfloor\frac{n!}{\mathrm{e}} + \frac{1}{2}\right\rfloor
$$

Kako broj elemenata raste, vjerojatnost P da je permutacija deranžman teži prema:

$$
P=\lim_{n\to\infty}\frac{D_n}{n!}=\frac{1}{\mathrm{e}}
$$
