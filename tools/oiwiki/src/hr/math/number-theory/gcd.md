---
title: Najveći zajednički djelitelj
---

## Definicija

Najveći zajednički djelitelj (engl. Greatest Common Divisor) obično se skraćeno označava gcd.

Zajednički djelitelj skupa cijelih brojeva jest broj koji je istodobno djelitelj svakog broja iz tog skupa. $\pm 1$ je zajednički djelitelj svakog skupa cijelih brojeva.

Najveći zajednički djelitelj skupa cijelih brojeva jest najveći među svim njihovim zajedničkim djeliteljima.

Za cijele brojeve $a,b$ koji nisu oba $0$ njihov najveći zajednički djelitelj označavamo $\gcd(a,b)$, a kad nema opasnosti od zabune skraćeno $(a,b)$.

Za cijele brojeve $a_1,\dots,a_n$ koji nisu svi $0$ njihov najveći zajednički djelitelj označavamo $\gcd(a_1,\dots,a_n)$, a kad nema opasnosti od zabune skraćeno $(a_1,\dots,a_n)$.

Svojstva najvećeg zajedničkog djelitelja i najmanjeg zajedničkog višekratnika vidi u [Osnovama teorije brojeva](./basic.md#najveći-zajednički-djelitelj-i-najmanji-zajednički-višekratnik).

Kako, dakle, izračunati najveći zajednički djelitelj? Razmotrimo najprije slučaj dvaju brojeva.

### Euklidov algoritam

#### Postupak

Ako su nam poznata dva broja $a$ i $b$, kako izračunati njihov najveći zajednički djelitelj?

Bez smanjenja općenitosti neka je $a > b$.

Uočavamo: ako je $b$ djelitelj od $a$, onda je $b$ njihov najveći zajednički djelitelj.
Razmotrimo sada slučaj kada dijeljenje nije bez ostatka, tj. $a = b \times q + r$, gdje je $r < b$.

Dokazom možemo dobiti $\gcd(a,b)=\gcd(b,a \bmod b)$; postupak je sljedeći:

???+ note "Dokaz"
    Neka je $a=bk+c$; očito je $c=a \bmod b$. Neka $d \mid a,~d \mid b$; tada je $c=a-bk, \frac{c}{d}=\frac{a}{d}-\frac{b}{d}k$.
    
    Iz desne strane vidimo da je $\frac{c}{d}$ cijeli broj, tj. $d \mid c$, pa je svaki zajednički djelitelj od $a,b$ ujedno zajednički djelitelj od $b,a \bmod b$.
    
    Treba dokazati i obrat:
    
    Neka $d \mid b,~d\mid (a \bmod b)$; kao i prije dobivamo $\frac{a\bmod b}{d}=\frac{a}{d}-\frac{b}{d}k,~\frac{a\bmod b}{d}+\frac{b}{d}k=\frac{a}{d}$.
    
    Budući da je lijeva strana očito cijeli broj, i $\frac{a}{d}$ je cijeli broj, tj. $d \mid a$, pa je svaki zajednički djelitelj od $b,a\bmod b$ ujedno zajednički djelitelj od $a,b$.
    
    Budući da su zajednički djelitelji obaju parova isti, isti su i najveći zajednički djelitelji.
    
    Time dobivamo formulu $\gcd(a,b)=\gcd(b,a\bmod b)$

Budući da smo dobili $\gcd(a, b) = \gcd(b, r)$, pri čemu se veličina dvaju brojeva ne povećava, dobili smo rekurzivni postupak za najveći zajednički djelitelj dvaju brojeva.

#### Implementacija

=== "C++"
    ```cpp
    // Version 1
    int gcd(int a, int b) {
      if (b == 0) return a;
      return gcd(b, a % b);
    }
    
    // Version 2
    int gcd(int a, int b) { return b == 0 ? a : gcd(b, a % b); }
    ```

=== "Java"
    ```java
    // Version 1
    public int gcd(int a, int b) {
        if (b == 0) return a;
        return gcd(b, a % b);
    }
    
    // Version 2
    public int gcd(int a, int b) {
        return b == 0 ? a : gcd(b, a % b);
    }
    ```

=== "Python"
    ```python
    def gcd(a, b):
        if b == 0:
            return a
        return gcd(b, a % b)
    ```

Rekurzija ide do slučaja `b == 0` (tj. `a % b == 0` u prethodnom koraku) i tada vraća vrijednost.

Na temelju gornjeg rekurzivnog postupka možemo napisati i iterativni:

=== "C++"
    ```cpp
    int gcd(int a, int b) {
      while (b != 0) {
        int tmp = a;
        a = b;
        b = tmp % b;
      }
      return a;
    }
    ```

=== "Java"
    ```java
    public int gcd(int a, int b) {
        while(b != 0) {
            int tmp = a;
            a = b;
            b = tmp % b;
        }
        return a;
    }
    ```

=== "Python"
    ```python
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a
    ```

Svi gornji algoritmi mogu se nazvati Euklidovim algoritmom (Euclidean algorithm).

Osim toga, u C++17 možemo koristiti [`std::gcd`](https://en.cppreference.com/w/cpp/numeric/gcd) i [`std::lcm`](https://en.cppreference.com/w/cpp/numeric/lcm) iz zaglavlja [`<numeric>`](https://en.cppreference.com/w/cpp/header/numeric) za računanje najvećeg zajedničkog djelitelja i najmanjeg zajedničkog višekratnika.

???+ warning "Napomena"
    U nekim prevoditeljima u C++14 najveći zajednički djelitelj može se računati funkcijom `std::__gcd(a,b)`, ali ona je samo privatna pomoćna funkcija za `std::rotate`.[^1]Korištenje te funkcije može dovesti do neočekivanih problema, pa se u pravilu ne preporučuje.

Ako dva broja $a$ i $b$ zadovoljavaju $\gcd(a, b) = 1$, kažemo da su $a$ i $b$ relativno prosti.

#### Svojstva

Koliko je Euklidov algoritam vremenski učinkovit? U nastavku dokazujemo da je, kad su ulaz dva binarna cijela broja duljine $n$, vremenska složenost Euklidova algoritma $O(n)$. (Drugim riječima, uz uobičajenu pretpostavku da su $a, b$ istog reda veličine, vremenska je složenost $O(\log\max(a, b))$.)

???+ note "Dokaz"
    Kad računamo $\gcd(a,b)$, susrećemo dva slučaja:
    
    -   $a < b$; tada je $\gcd(a,b)=\gcd(b,a)$;
    -   $a \geq b$; tada je $\gcd(a,b)=\gcd(b,a \bmod b)$, a uzimanje ostatka od $a$ barem prepolovi $a$. To znači da se ovaj korak može dogoditi najviše $O(\log a) = O(n)$ puta.
    
    Nakon prvog slučaja sigurno slijedi drugi slučaj, pa se prvi slučaj događa **ne više puta** od drugoga.
    
    Stoga rezultat dobivamo nakon najviše $O(n)$ rekurzivnih poziva.

Zapravo, ako Euklidovim algoritmom pokušamo izračunati najveći zajednički djelitelj dvaju susjednih članova [Fibonaccijeva niza](../combinatorics/fibonacci.md), algoritam dostiže najgoru složenost.

### Metoda uzastopnog oduzimanja (更相减损术)

Uzimanje ostatka kod velikih cijelih brojeva ima veliku vremensku složenost, a zbrajanje i oduzimanje malu. Za velike cijele brojeve najveći zajednički djelitelj možemo izračunati zbrajanjem i oduzimanjem umjesto množenjem i dijeljenjem.

#### Postupak

Zadani su brojevi $a$ i $b$; tražimo $\gcd(a,b)$.

Bez smanjenja općenitosti neka je $a \ge b$. Ako je $a = b$, onda je $\gcd(a,b)=a=b$.
Inače, $\forall d\mid a, d\mid b$ može se dokazati $d\mid a-b$.

Stoga su **svi** zajednički djelitelji od $a$ i $b$ ujedno zajednički djelitelji od $a-b$ i $b$, pa je $\gcd(a,b) = \gcd(a-b, b)$.

#### Optimizacija: Steinov algoritam

Ako je $a\gg b$, složenost $O(n)$ metode uzastopnog oduzimanja dostiže najgori slučaj.

Razmotrimo optimizaciju: ako $2\mid a,2\mid b$, onda je $\gcd(a,b) = 2\gcd\left(\dfrac a2, \dfrac b2\right)$.

Inače, ako $2\mid a$ (slučaj $2\mid b$ analogno), budući da je slučaj $2\mid b$ već razmotren, vrijedi $2 \nmid b$. Stoga je $\gcd(a,b)=\gcd\left(\dfrac a2,b\right)$.

Vremenska složenost optimiziranog algoritma (tj. Steinova algoritma) je $O(\log n)$.

???+ note "Dokaz"
    Ako $2\mid a$ ili $2\mid b$, svaki rekurzivni korak barem jedan od $a,b$ prepolovi.
    
    Inače $2\mid a-b$, čime se vraćamo na prethodni slučaj.
    
    Algoritam ima najviše $O(\log n)$ rekurzivnih poziva.

#### Implementacija

Predložak za velike brojeve vidi u [Aritmetici velikih brojeva](../bignum.md).

Za velike brojeve treba implementirati: oduzimanje, usporedbu, pomak ulijevo, pomak udesno (mogu se zamijeniti množenjem/dijeljenjem malim brojem) i broj nula na kraju binarnog zapisa (može se izračunati grubom silom provjerom parnosti).

??? note "C++"
    ```cpp
    Big gcd(Big a, Big b) {
      if (a == 0) return b;
      if (b == 0) return a;
      // bilježimo koliko se puta 2 pojavljuje kao zajednički faktor od a i b; countr_zero je broj nula na kraju binarnog zapisa
      int atimes = countr_zero(a);
      int btimes = countr_zero(b);
      int mintimes = min(atimes, btimes);
      a >>= atimes;
      for (;;) {
        // dvojke iz zajedničkih faktora od a i b već su obrađene, pa a dalje ne može biti paran
        b >>= btimes;
        // osiguravamo a<=b
        if (a > b) swap(a, b);
        b -= a;
        if (b == 0) break;
        btimes = countr_zero(b);
      }
      return a << mintimes;
    }
    ```

Gornji kod slijedi implementacije C++17 `std::gcd` u [libstdc++](https://github.com/gcc-mirror/gcc/blob/1667962ae755db27965778b8c8c684c6c0c4da21/libstdc%2B%2B-v3/include/std/numeric#L173) i [MSVC](https://github.com/microsoft/STL/blob/9aca22477df4eed3222b4974746ee79129eb44e7/stl/inc/numeric#L591). U rasponu tipova `unsigned int` i `unsigned long long`, ako se `countr_zero` može izračunati vrlo brzo, Steinov je algoritam brži od Euklidova, a inače može biti i sporiji od Euklidova.

???+ note "O funkciji countr_zero"
    1.  gcc ima [ugrađene funkcije](../bit.md#ugrađene-funkcije-gcc-a) `__builtin_ctz` (32-bitnu) i `__builtin_ctzll` (64-bitnu) koje mogu zamijeniti `countr_zero` u gornjem kodu;
    2.  Od C++20 zaglavlje `<bit>` sadrži [`std::countr_zero`](https://en.cppreference.com/w/cpp/numeric/countr_zero);
    3.  Ako ne želite koristiti funkcije izvan standardne knjižnice, a ne možete koristiti standard C++20, sljedeći je kod implementacija koja u modelu Word-RAM with multiplication nakon pretprocesiranja radi u $O(1)$:
    
    ```cpp
    constexpr int loghash[64] = {0,  32, 48, 56, 60, 62, 63, 31, 47, 55, 59, 61, 30,
                                 15, 39, 51, 57, 28, 46, 23, 43, 53, 58, 29, 14, 7,
                                 35, 49, 24, 44, 54, 27, 45, 22, 11, 37, 50, 25, 12,
                                 38, 19, 41, 52, 26, 13, 6,  3,  33, 16, 40, 20, 42,
                                 21, 10, 5,  34, 17, 8,  36, 18, 9,  4,  2,  1};
    
    int countr_zero(unsigned long long x) {
      return loghash[(x & -x) * 0x9150D32D8EB9EFC0Ui64 >> 58];
    }
    ```
    
    Kod velikih brojeva, ako je implementacija slična `bitset`u, uz gornju implementaciju `countr_zero` to se može obaviti u vremenskoj složenosti `O(n / w)`. Ako pak nije zgodno dijeliti po binarnim bitovima, najveću potenciju broja $2$ koja dijeli broj možemo odrediti samo grubom silom, a vremenska složenost ovisi o implementaciji. Na primjer:
    
    ```cpp
    // binarni Big u little-endian poretku; mora se moći proći kroz svaki element
    int countr_zero(Big a) {
      int ans = 0;
      for (auto x : a) {
        if (x != 0) {
          ans += 32;  // broj bitova tipa podataka jednog elementa
        } else {
          return ans + countr_zero(x);
        }
      }
      return ans;
    }
    
    // izračun grubom silom; ako se koristi, preporučuje se ugraditi ga izravno u gcd radi bolje konstante
    int countr_zero(Big a) {
      int ans = 0;
      while ((a & 1) == 0) {
        a >>= 1;
        ++ans;
      }
      return ans;
    }
    ```

Više rasprave o brzini raznih implementacija `gcd` možete pročitati u [Fastest way to compute the greatest common divisor](https://lemire.me/blog/2013/12/26/fastest-way-to-compute-the-greatest-common-divisor/).

### Najveći zajednički djelitelj više brojeva

Kako pak izračunati najveći zajednički djelitelj više brojeva? Odgovor je očito djelitelj svakog od brojeva, pa je sigurno i djelitelj svaka dva susjedna broja. Indukcijom se može dokazati da uzimanje dvaju brojeva, računanje njihova rezultata i vraćanje tog rezultata natrag ne utječe na traženi odgovor.

## Najmanji zajednički višekratnik

Sada ćemo pokazati kako izračunati najmanji zajednički višekratnik (Least Common Multiple, LCM).

### Definicija

Zajednički višekratnik skupa cijelih brojeva jest broj koji je istodobno višekratnik svakog broja iz tog skupa. 0 je zajednički višekratnik svakog skupa cijelih brojeva.

Najmanji zajednički višekratnik skupa cijelih brojeva jest najmanji među svim pozitivnim zajedničkim višekratnicima.

Za cijele brojeve $a,b$ njihov najmanji zajednički višekratnik označavamo $\operatorname{lcm}(a,b)$, a kad nema opasnosti od zabune skraćeno $[a,b]$.

Za cijele brojeve $a_1,\dots,a_n$ njihov najmanji zajednički višekratnik označavamo $\operatorname{lcm}(a_1,\dots,a_n)$, a kad nema opasnosti od zabune skraćeno $[a_1,\dots,a_n]$.

### Dva broja

Neka je $a = p_1^{k_{a_1}}p_2^{k_{a_2}} \cdots p_s^{k_{a_s}}$, $b = p_1^{k_{b_1}}p_2^{k_{b_2}} \cdots p_s^{k_{b_s}}$

Uočavamo da je za $a$ i $b$ njihov najveći zajednički djelitelj jednak

$p_1^{\min(k_{a_1}, k_{b_1})}p_2^{\min(k_{a_2}, k_{b_2})} \cdots p_s^{\min(k_{a_s}, k_{b_s})}$

a najmanji zajednički višekratnik jednak

$p_1^{\max(k_{a_1}, k_{b_1})}p_2^{\max(k_{a_2}, k_{b_2})} \cdots p_s^{\max(k_{a_s}, k_{b_s})}$

Budući da je $k_a + k_b = \max(k_a, k_b) + \min(k_a, k_b)$

dobivamo zaključak $\gcd(a, b) \times \operatorname{lcm}(a, b) = a \times b$

Da bismo izračunali najmanji zajednički višekratnik dvaju brojeva, dovoljno je najprije izračunati najveći zajednički djelitelj.

### Više brojeva

Vidimo da je, kad izračunamo $\gcd$ dvaju brojeva, računanje najmanjeg zajedničkog višekratnika složenosti $O(1)$. Za više brojeva zapravo nije potrebno računati zajednički najveći zajednički djelitelj pa onda dalje obrađivati; najizravniji je način ovaj: kao što pri računanju $\gcd$ više brojeva, nakon što izračunamo $\gcd$ dvaju brojeva, rezultat vraćamo u niz i nastavljamo s preostalim brojevima, tako i ovdje, analogno, u niz izravno stavimo najmanji zajednički višekratnik.

## Prošireni Euklidov algoritam

Prošireni Euklidov algoritam (Extended Euclidean algorithm, EXGCD) često se koristi za nalaženje jednog rješenja jednadžbe $ax+by=\gcd(a,b)$.

### Postupak

Neka je

$ax_1+by_1=\gcd(a,b)$

$bx_2+(a\bmod b)y_2=\gcd(b,a\bmod b)$

Po Euklidovu teoremu: $\gcd(a,b)=\gcd(b,a\bmod b)$

pa je $ax_1+by_1=bx_2+(a\bmod b)y_2$

Osim toga, $a\bmod b=a-(\lfloor\frac{a}{b}\rfloor\times b)$

pa je $ax_1+by_1=bx_2+(a-(\lfloor\frac{a}{b}\rfloor\times b))y_2$

$ax_1+by_1=ay_2+bx_2-\lfloor\frac{a}{b}\rfloor\times by_2=ay_2+b(x_2-\lfloor\frac{a}{b}\rfloor y_2)$

Budući da je $a=a,b=b$, slijedi $x_1=y_2,y_1=x_2-\lfloor\frac{a}{b}\rfloor y_2$

Uvrštavamo $x_2,y_2$ rekurzivno sve dok $b$ ne postane $0$, kada je $x=1,y=0$, a zatim se vraćamo natrag i računamo rješenje.

### Implementacija

=== "C++"
    ```cpp
    int Exgcd(int a, int b, int &x, int &y) {
      if (!b) {
        x = 1;
        y = 0;
        return a;
      }
      int d = Exgcd(b, a % b, x, y);
      int t = x;
      x = y;
      y = t - (a / b) * y;
      return d;
    }
    ```

=== "Python"
    ```python
    def Exgcd(a, b):
        if b == 0:
            return a, 1, 0
        d, x, y = Exgcd(b, a % b)
        return d, y, x - (a // b) * y
    ```

Funkcija vraća $\gcd$, a usput računa $x,y$.

### Analiza raspona vrijednosti

Jednadžba $ax+by=\gcd(a,b)$ ima beskonačno mnogo rješenja i očito neka od njih prekoračuju long long.  
Srećom, ako je $b\not= 0$, rješenje koje daje prošireni Euklidov algoritam sigurno zadovoljava $|x|\le b,|y|\le a$.  
Slijedi dokaz tog svojstva.

??? note "Dokaz"
    -   Kad je $\gcd(a,b)=b$, vrijedi $a\bmod b=0$, pa rekurzija sigurno završava na sljedećoj razini.  
        Dobivamo $x_1=0,y_1=1$ i očito $a,b\ge 1\ge |x_1|,|y_1|$.
    -   Kad je $\gcd(a,b)\not= b$, pretpostavimo $|x_2|\le (a\bmod b),|y_2|\le b$.  
        Budući da je $x_1=y_2,y_1=x_2-{\left\lfloor\dfrac{a}{b}\right\rfloor}y_2$   
        vrijedi $|x_1|=|y_2|\le b,|y_1|\le|x_2|+|{\left\lfloor\dfrac{a}{b}\right\rfloor}y_2|\le (a\bmod b)+{\left\lfloor\dfrac{a}{b}\right\rfloor}|y_2|$  
        $\le a-{\left\lfloor\dfrac{a}{b}\right\rfloor}b+{\left\lfloor\dfrac{a}{b}\right\rfloor}|y_2|\le a-{\left\lfloor\dfrac{a}{b}\right\rfloor}(b-|y_2|)$   
        $a\bmod b=a-{\left\lfloor\dfrac{a}{b}\right\rfloor}b\le a-{\left\lfloor\dfrac{a}{b}\right\rfloor}(b-|y_2|)\le a$   
        Stoga vrijedi $|x_1|\le b,|y_1|\le a$.

### Iterativna izvedba proširenog Euklidova algoritma

Najprije, za $x = 1$, $y = 0$, $x_1 = 0$, $y_1 = 1$ očito vrijedi:

$$
\begin{cases}
    ax + by     & = a \\
    ax_1 + by_1 & = b
\end{cases}
$$

Znamo da je $a\bmod b = a - (\lfloor \frac{a}{b} \rfloor \times b)$; označimo $q = \lfloor \frac{a}{b} \rfloor$. Po uzoru na iterativno računanje gcd-a, svaki korak iteracije možemo zapisati kao:

$$
(a, b) \rightarrow (b, a - qb)
$$

Zamijenimo li u iteraciji $a$ s $ax + by = a$, a $b$ s $ax_1 + by_1 = b$, dobivamo:

$$
\begin{aligned}
                & \begin{cases}
                      ax + by     & = a \\
                      ax_1 + by_1 & = b
                  \end{cases}                    \\
    \rightarrow & \begin{cases}
                      ax_1 + by_1               & = b      \\
                      a(x - qx_1) + b(y - qy_1) & = a - qb
                  \end{cases}
\end{aligned}
$$

Na temelju toga dobivamo iterativni exgcd.

Budući da iterativna metoda izbjegava rekurziju, kod će se izvršavati nešto brže od rekurzivnog.

```cpp
int gcd(int a, int b, int& x, int& y) {
  x = 1, y = 0;
  int x1 = 0, y1 = 1, a1 = a, b1 = b;
  while (b1) {
    int q = a1 / b1;
    tie(x, x1) = make_tuple(x1, x - q * x1);
    tie(y, y1) = make_tuple(y1, y - q * y1);
    tie(a1, b1) = make_tuple(b1, a1 - q * b1);
  }
  return a1;
}
```

Pogledate li pažljivo $a_1$ i $b_1$, primijetit ćete da poprimaju potpuno iste vrijednosti kao u iterativnoj inačici Euklidova algoritma, te da sljedeće formule vrijede u svakom trenutku (prije petlje while i na kraju svake iteracije): $x \cdot a +y \cdot b =a_1$ i $x_1 \cdot a +y_1 \cdot b= b_1$. Stoga algoritam sigurno ispravno računa $\gcd$.

Na kraju znamo da je $a_1$ upravo traženi $\gcd$, pa vrijedi $x \cdot a +y \cdot b = g$.

#### Matrično tumačenje

Jedan korak Euklidova algoritma za pozitivne cijele brojeve $a$ i $b$, tj. $\gcd(a,b)=\gcd(b,a\bmod b)$, matrično se zapisuje kao

$$
\begin{bmatrix}
b\\a\bmod b
\end{bmatrix}
=
\begin{bmatrix}
0&1\\1&-\lfloor a/b\rfloor
\end{bmatrix}
\begin{bmatrix}
a\\b
\end{bmatrix}
$$

gdje oznaka donjeg cijelog dijela $\lfloor c\rfloor$ označava najveći cijeli broj koji nije veći od $c$. Definiramo transformaciju $\begin{bmatrix}a\\b\end{bmatrix}\mapsto \begin{bmatrix}0&1\\1&-\lfloor a/b\rfloor\end{bmatrix}\begin{bmatrix}a\\b\end{bmatrix}$.

Lako se vidi da je Euklidov algoritam upravo uzastopna primjena te transformacije, pa vrijedi

$$
\begin{bmatrix}
\gcd(a,b)\\0
\end{bmatrix}
=
\left(
\cdots 
\begin{bmatrix}
0&1\\1&-\lfloor a/b\rfloor
\end{bmatrix}
\begin{bmatrix}
1&0\\0&1
\end{bmatrix}
\right)
\begin{bmatrix}
a\\b
\end{bmatrix}
$$

Neka je

$$
\begin{bmatrix}
x_1&x_2\\x_3&x_4
\end{bmatrix}
=
\cdots 
\begin{bmatrix}
0&1\\1&-\lfloor a/b\rfloor
\end{bmatrix}
\begin{bmatrix}
1&0\\0&1
\end{bmatrix}
$$

Tada je

$$
\begin{bmatrix}
\gcd(a,b)\\0
\end{bmatrix}
=
\begin{bmatrix}
x_1&x_2\\x_3&x_4
\end{bmatrix}
\begin{bmatrix}
a\\b
\end{bmatrix}
$$

i vrijedi $a\cdot x_1+b\cdot x_2=\gcd(a,b)$, što je upravo prošireni Euklidov algoritam. Primijetite da množenje jediničnom matricom na kraju ne utječe na rezultat, što nam sugerira da na početku možemo održavati jediničnu matricu $2\times 2$ i napisati sažetiju iterativnu inačicu:

```cpp
int exgcd(int a, int b, int &x, int &y) {
  int x1 = 1, x2 = 0, x3 = 0, x4 = 1;
  while (b != 0) {
    int c = a / b;
    std::tie(x1, x2, x3, x4, a, b) =
        std::make_tuple(x3, x4, x1 - x3 * c, x2 - x4 * c, b, a - b * c);
  }
  x = x1, y = x2;
  return a;
}
```

Ovaj je prikaz jednostavniji od rekurzivnog.

## Primjene

-   [10104 - Euclid Problem](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=1045)
-   [GYM - (J) once upon a time](http://codeforces.com/gym/100963)
-   [UVa - 12775 - Gift Dilemma](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=4628)

## Literatura i poveznice

[^1]: [libstdc++: std Namespace Reference](https://gcc.gnu.org/onlinedocs/libstdc++/libstdc++-html-USERS-4.4/a00978.html#a2686a128df5a576cb53a1ed5f674607)
