---
title: Operacije nad skupovima u binarnom zapisu
---

Preduvjeti: [Logičke operacije po bitovima](./bit.md#logičke-operacije-po-bitovima), [Cijeli brojevi i nizovi bitova](./bit.md#cijeli-brojevi-i-nizovi-bitova).

Binarni zapis broja možemo promatrati kao skup ($0$ znači da element nije u skupu, $1$ da jest). Primjerice, skup $\{1,3,4,8\}$ može se prikazati kao $(100011010)_2$. Odgovarajuće operacije po bitovima tada možemo promatrati kao operacije nad skupovima.

| Operacija   |    Skupovni zapis     |         Zapis operacijama po bitovima          |
| ------ | :-------------: | :-------------------------: |
| presjek   |   $a \cap b$    | $a \operatorname{AND} b$ |
| unija   |   $a \cup b$    | $a \operatorname{OR} b$ |
| komplement   |    $\bar{a}$    | $\operatorname{NOT} a$ (univerzalni skup ima sve bitove jednake 1) |
| razlika   | $a \setminus b$ | $a \operatorname{AND} \operatorname{NOT} b$ |
| simetrična razlika | $a\triangle b$  | $a \operatorname{XOR} b$  |

Prije nego što prijeđemo na obilazak podskupova skupa, pogledajmo nekoliko primjera primjene operacija po bitovima.

### Modulo potencija broja 2

Uzimanje ostatka broja pri dijeljenju nenegativnom cjelobrojnom potencijom broja $2$ ekvivalentno je uzimanju posljednjih nekoliko bitova binarnog zapisa tog broja, odnosno operaciji AND s $mod-1$.

=== "C++"
    ```cpp
    int modPowerOfTwo(int x, int mod) { return x & (mod - 1); }
    ```

=== "Python"
    ```python
    def modPowerOfTwo(x, mod):
        return x & (mod - 1)
    ```

Odatle slijedi da nenegativna cjelobrojna potencija broja $2$ pri dijeljenju samom sobom daje ostatak $0$, tj. ako je $n$ nenegativna cjelobrojna potencija broja $2$, rezultat operacije AND nad $n$ i $n-1$ jest $0$.

Zapravo, za pozitivan cijeli broj $n$, $n-1$ postavlja najniži bit $1$ broja $n$ na nulu, a sve bitove iza njega na $1$. Stoga je AND nad $n$ i $n-1$ ekvivalentan brisanju najnižeg bita $1$ broja $n$.

Time možemo provjeriti je li broj nenegativna cjelobrojna potencija broja $2$: $n$ je nenegativna cjelobrojna potencija broja $2$ ako i samo ako binarni zapis od $n$ sadrži točno jednu jedinicu $1$.

=== "C++"
    ```cpp
    bool isPowerOfTwo(int n) { return n > 0 && (n & (n - 1)) == 0; }
    ```

=== "Python"
    ```python
    def isPowerOfTwo(n):
        return n > 0 and (n & (n - 1)) == 0
    ```

### Obilazak podskupova

Obilazak svih podskupova skupa prikazanog binarnim brojem ekvivalentan je nabrajanju svih podmaski maske koja odgovara tom binarnom broju.

Maska je niz bitova koji se operacijom AND primjenjuje na izvorni niz, čime se dobiva novi operand u kojem je nekoliko ulaznih bitova izvornog niza maskirano.

Maska na izvorni niz djeluje kao zaslon: bit $1$ u maski znači da se odgovarajući bit izvornog niza zadržava, a bit $0$ u maski znači da se odgovarajući bit izvornog niza postavlja na $0$. Zamjenom nekoliko bitova $1$ maske bitovima $0$ dobivamo podmasku te maske; maska je i sama svoja podmaska.

Za zadanu masku $m$ želimo učinkovito iterirati po svim podmaskama $s$ maske $m$; možemo razmotriti implementaciju zasnovanu na trikovima s operacijama po bitovima.

```cpp
// obilazak nepraznih podskupova od m u silaznom poretku
int s = m;
while (s > 0) {
  // s je neprazan podskup od m
  s = (s - 1) & m;
}
```

Ili kompaktnijom naredbom for:

```cpp
// obilazak nepraznih podskupova od m u silaznom poretku
for (int s = m; s; s = (s - 1) & m)
// s je neprazan podskup od m
```

Nijedan od ova dva odsječka koda ne obrađuje podmasku jednaku $0$; želimo li obraditi i podmasku jednaku $0$, možemo upotrijebiti druge načine, npr.:

```cpp
// obilazak podskupova od m u silaznom poretku
for (int s = m;; s = (s - 1) & m) {
  // s je podskup od m
  if (s == 0) break;
}
```

Dokažimo sada da gornji kod posjećuje sve podmaske od $m$, bez ponavljanja i u silaznom poretku.

Pretpostavimo da imamo trenutačnu bitovnu masku $s$ i želimo posjetiti sljedeću bitovnu masku. Oduzimanje $1$ od maske $s$ ekvivalentno je uklanjanju krajnjeg desnog postavljenog bita maske $s$ i postavljanju svih bitova desno od njega na $1$.

Da bi $s-1$ postao nova podmaska, treba ukloniti sve dodatne bitove $1$ koji nisu sadržani u maski $m$; to uklanjanje izvodi se operacijom po bitovima `(s - 1) & m`.

Ta su dva koraka ekvivalentna „odrezivanju” maske $s-1$ kako bi se odredila najveća aritmetički dostižna vrijednost, tj. sljedeća podmaska nakon $s$ u silaznom poretku.

Dakle, algoritam generira sve podmaske te maske u silaznom poretku, izvodeći u svakoj iteraciji samo dvije operacije.

Poseban je slučaj $s=0$. Nakon izvođenja $s-1$ dobivamo $-1$, kojemu su svi bitovi jednaki $1$. Nakon operacije `(s - 1) & m` novi $s$ bit će jednak $m$. Stoga, ako petlja ne završava pri $s=0$, petlja algoritma neće se zaustaviti.

Označimo li s $\text{popcount}(m)$ broj jedinica $1$ u binarnom zapisu od $m$, ovom metodom podskupove skupa $m$ možemo obići u vremenskoj složenosti $O(2^{\text{popcount}(m)})$.

### Obilazak podmaski svih maski

U zadacima s DP-om s bitmaskama ponekad za svaku masku želimo obići sve njezine podmaske:

```cpp
for (int m = 0; m < (1 << n); ++m)
  // obilazak nepraznih podskupova od m u silaznom poretku
  for (int s = m; s; s = (s - 1) & m)
// s je neprazan podskup od m
```

Tako obilazimo podskupove svakog podskupa skupa veličine $n$.

Dokažimo sada da je vremenska složenost tog postupka $O(3^n)$, gdje je $n$ ukupan broj bitova maske, tj. ukupan broj elemenata skupa.

Promotrimo $i$-ti bit, tj. $i$-ti element skupa; postoje tri slučaja:

- u maski $m$ je $0$, pa je i u podmaski $s$ jednak $0$, tj. element nije ni u većem ni u manjem podskupu;
- u $m$ je $1$, ali u $s$ je $0$, tj. element je samo u većem podskupu, a ne i u manjem;
- u $m$ i u $s$ je $1$, tj. element je i u većem i u manjem podskupu.

Ukupno je $n$ bitova, pa postoji $3^n$ različitih kombinacija.

Postoji i drugi način dokaza:

Ako maska $m$ ima $k$ jedinica $1$, onda ima $2^k$ podmaski. Za zadani $k$ postoji $\dbinom{n}{k}$ odgovarajućih maski $m$, pa je ukupan broj svih maski:

$$
\sum_{k=0}^n \dbinom{n}{k} 2^k
$$

Gornja suma jednaka je razvoju $(1+2)^n$ po binomnom teoremu, pa postoji $3^n$ različitih kombinacija.

### Literatura

**Ova je stranica uglavnom prevedena iz članka [Перебор всех подмасок данной маски](http://e-maxx.ru/algo/all_submasks) i njegova engleskog prijevoda [Submask Enumeration](https://cp-algorithms.com/algebra/all-submasks.html). Ruska je inačica objavljena pod licencijom Public Domain + Leave a Link, a engleska pod CC-BY-SA 4.0.**

### Zadaci za vježbu

- [Atcoder - Close Group](https://atcoder.jp/contests/abc187/tasks/abc187_f)
- [Codeforces - Nuclear Fusion](http://codeforces.com/problemset/problem/71/E)
- [Codeforces - Sandy and Nuts](http://codeforces.com/problemset/problem/599/E)
- [UVa 1439 - Exclusive Access 2](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=4185)
- [UVa 11825 - Hackers' Crackdown](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=2925)
