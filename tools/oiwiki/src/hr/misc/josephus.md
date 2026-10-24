---
title: Josephusov problem
---

Josephusov problem postoji već jako dugo, a i rješenja tog problema stalno se poboljšavaju; ipak, još uvijek ne postoji iznimno učinkovit algoritam (unutar logaritamske složenosti) koji bi ga riješio.

## Opis problema

> n ljudi označeno je brojevima $0,1,\cdots, n-1$. Stoje u krugu u smjeru suprotnom od kazaljke na satu; počevši od osobe $0$, svaki se put od trenutne osobe u smjeru suprotnom od kazaljke na satu odbroji $k$ ljudi i ta osoba ispada iz igre. Pitanje je tko ostaje posljednji.

Ovaj je klasični problem postavio Josip Flavije (Josephus) u 1. stoljeću, iako je on tada razmatrao samo slučaj $k=2$. Danas ga možemo riješiti mnogim učinkovitim algoritmima.

## Postupak

### Naivni algoritam

Najnaivniji je algoritam, naravno, izravna simulacija. Kružnom vezanom listom simuliramo postupak izbacivanja; ponovimo ga $n-1$ puta i dobijemo odgovor. Složenost je $\Theta (n^2)$.

### Jednostavna optimizacija

Traženje sljedeće osobe može se optimizirati segment treeom. Konkretno, izgradimo segment tree nad $0,1,\cdots, n-1$ i u njemu pamtimo broj preostalih ljudi u svakom intervalu. Položaj trenutne osobe i $k$-tu osobu nakon nje tada možemo pronaći binarnim pretraživanjem po segment treeu.

### Linearni algoritam

Neka $J_{n,k}$ označava odgovor na Josephusov problem s parametrima $n,k$. Vrijedi sljedeća rekurzija

$$
J_{n,k}=(J_{n-1,k}+k)\bmod n
$$

I nju je lako izvesti. Krenemo od $0$ i odbrojimo $k$ ljudi; nakon što osoba $k-1$ ispadne, ostaje $n-1$ ljudi. Kad izračunamo odgovor za tih $n-1$ ljudi, dodamo još relativni pomak $k$ i dobijemo pravi odgovor. Složenost ovog algoritma očito je $\Theta (n)$.

???+ note "Implementacija"
    ```cpp
    int josephus(int n, int k) {
      int res = 0;
      for (int i = 1; i <= n; ++i) res = (res + k) % i;
      return res;
    }
    ```

### Logaritamski algoritam

Za slučaj kad je $k$ malen, a $n$ velik, postoji i algoritam složenosti $\Theta (k\log n)$.

Budući da svaki put odbrojimo $k$ ljudi i jednoga izbacimo, unutar jednog kruga možemo izbaciti $\left\lfloor\frac{n}{k}\right\rfloor$ ljudi, nakon čega ostaje $n-\left\lfloor\frac{n}{k}\right\rfloor$ ljudi. Tada se nalazimo na položaju $\left\lfloor\frac{n}{k}\right\rfloor\cdot k$-te osobe, a lako je uočiti da je to jednako $n-n\bmod k$. Zatim nastavljamo rekurzivno, a nakon izračuna vraćamo relativni položaj. Vraćanje relativnog položaja temelji se na sljedećem: svako izbacivanje uklanja odbrojanu $k$-tu osobu, a njezinu oznaku jedan po jedan nasljeđuju ljudi iza nje; drugim riječima, kad računamo s krugom od $n-\left\lfloor\frac{n}{k}\right\rfloor$ ljudi, na svakih $k$ ljudi položaj $1$ osobe nije uračunat. Zato, ako je rezultat manji od $0$, uzmemo ga modulo $n$ u krugu od $n$ ljudi iz kojega još nisu izbačene oznake koje su višekratnici od $k$; ako je rezultat veći ili jednak $0$, možemo ga izravno pomnožiti s $\frac{k}{k-1}$. Tako dobivamo sljedeći algoritam:

???+ note "Implementacija"
    ```cpp
    int josephus(int n, int k) {
      if (n == 1) return 0;
      if (k == 1) return n - 1;
      if (k > n) return (josephus(n - 1, k) + k) % n;  // linearni algoritam
      int res = josephus(n - n / k, k);
      res -= n % k;
      if (res < 0)
        res += n;  // mod n
      else
        res += res / (k - 1);  // vraćanje položaja
      return res;
    }
    ```

Može se dokazati da je složenost ovog algoritma $\Theta (k\log n)$. Neka je broj rekurzivnih poziva $x$; tada se u svakom koraku veličina problema otprilike smanji na $\displaystyle n\left(1-\frac{1}{k}\right)$, pa dobivamo

$$
n\left(1-\frac{1}{k}\right)^x=1
$$

Rješavanjem te jednadžbe dobivamo

$$
x=-\frac{\ln n}{\ln\left(1-\frac{1}{k}\right)}
$$

U nastavku dokazujemo da je složenost algoritma $\Theta (k\log n)$.

???+ note "Dokaz"
    Promotrimo $\displaystyle \lim _{k \rightarrow \infty} k \log \left(1-\frac{1}{k}\right)$; vrijedi
    
    $$
    \begin{aligned}
    \lim _{k \rightarrow \infty} k \log \left(1-\frac{1}{k}\right)&=\lim _{k \rightarrow \infty} \frac{\log \left(1-\frac{1}{k}\right)}{1 / k}\\
    &=\lim _{k \rightarrow \infty} \frac{\frac{\mathrm d}{\mathrm d k} \log \left(1-\frac{1}{k}\right)}{\frac{\mathrm d}{\mathrm d k}\left(\frac{1}{k}\right)}\\
    &=\lim _{k \rightarrow \infty} \frac{\frac{1}{k^{2}\left(1-\frac{1}{k}\right)}}{-\frac{1}{k^{2}}}\\
    &=\lim _{k \rightarrow \infty}-\frac{k}{k-1}\\
    &=-\lim _{k \rightarrow \infty} \frac{1}{1-\frac{1}{k}}\\
    &=-1
    \end{aligned}
    $$
    
    Dakle $x \sim k \ln n, k\to \infty$, tj. $-\dfrac{\ln n}{\ln\left(1-\frac{1}{k}\right)}= \Theta (k\log n)$

**Ova je stranica uglavnom prevedena iz članka [Задача Иосифа](https://e-maxx.ru/algo/joseph_problem) i njegova engleskog prijevoda [Josephus Problem](https://cp-algorithms.com/others/josephus_problem.html). Ruska je inačica objavljena pod licencijom Public Domain + Leave a Link, a engleska pod CC-BY-SA 4.0.**
