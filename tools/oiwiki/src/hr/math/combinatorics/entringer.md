---
title: Entringerovi brojevi
---

## Entringerovi brojevi

Entringerovi brojevi (Entringer numbers, [OEIS A008281](http://oeis.org/A008281)) $E(n,k)$ broj su permutacija $n+1$ brojeva od $0$ do $n$ koje zadovoljavaju sljedeće uvjete:

-   prvi element je $k$;
-   element nakon prvoga manji je od prvoga, sljedeći je element veći od prethodnoga, sljedeći je opet manji od prethodnoga… i odnosi veličina svih daljnjih susjednih elemenata slijede isto pravilo.

Početne vrijednosti Entringerovih brojeva jesu:

$$
E(0,0)=1
$$

$$
E(n,0)=0
$$

Vrijedi rekurzivna relacija:

$$
E(n,k)=E(n,k-1)+E(n-1,n-k)
$$

## Seidel–Entringer–Arnoldov trokut

Prikladno raspoređeni Entringerovi brojevi tvore brojevni trokut koji se naziva Seidel–Entringer–Arnoldov trokut (Seidel–Entringer–Arnold triangle, [OEIS A008280](http://oeis.org/A008280)). U tom su trokutu Entringerovi brojevi $E_(n,k)$ raspoređeni u „boustrofedonskom” redoslijedu (redoslijedu oranja volovima, engl. ox-plowing order):

$$
\begin{aligned}
& E(0,0) \\
& E(1,0) \rightarrow E(1,1) \\
& E(2,2) \leftarrow E(2,1) \leftarrow E(2,0) \\
& E(3,0) \rightarrow E(3,1) \rightarrow E(3,2) \rightarrow E(3,3) \\
& E(4,4) \leftarrow E(4,3) \leftarrow E(4,2) \leftarrow E(4,1) \leftarrow E(4,0)
\end{aligned}
$$

Odnosno:

$$
\begin{aligned}
& 1 \\
& 0 \rightarrow 1 \\
& 1 \leftarrow 1 \leftarrow 0 \\
& 0 \rightarrow 1 \rightarrow 2 \rightarrow 2 \\
& 5 \leftarrow 5 \leftarrow 4 \leftarrow 2 \leftarrow 0
\end{aligned}
$$

Prednost je ovakvog rasporeda Entringerovih brojeva to što je usklađen s njihovom rekurzivnom relacijom $E(n,k)=E(n,k-1)+E(n-1,n-k)$, pa ga je lako pamtiti i razumjeti.

Entringerovi brojevi imaju eksponencijalnu funkciju izvodnicu:

$$
\sum_{m=0}^\infty\sum_{n=0}^\infty E\left(m+n,\frac{1}{2}\left(m+n+{(-1)}^{m+n}(n-m)\right)\right)\frac{x^m}{m!}\frac{x^n}{n!}=\frac{\cos x+\sin x}{\cos (x+y)}
$$

Raspored koeficijenata ove funkcije izvodnice zapravo je samo jednostavno „razvučen” gornji Seidel–Entringer–Arnoldov trokut:

$$
\begin{array}{ccccc}
E(0,0) & E(1,1) & E(2,0) & E(3,3) & E(4,0) \\
E(1,0) & E(2,1) & E(3,2) & E(4,1) & \\
E(2,2) & E(3,1) & E(4,2) & & \\
E(3,0) & E(4,3) & & & \\
E(4,4) & & & &
\end{array}
$$

Odnosno:

$$
\begin{aligned}
& 1\quad 1\quad 0\quad 2\quad 0\\
& 0\quad 1\quad 2\quad 2\\
& 1\quad 1\quad 4\\
& 0\quad 5\\
& 5
\end{aligned}
$$

## Zigzag permutacije

Zigzag permutacija (zigzag permutation) permutacija je $c_1$ do $c_i$ brojeva od $1$ do $n$ u kojoj vrijednost nijednog elementa $c_i$ ne leži između $c_{i-1}$ i $c_{i+1}$.

Broj zigzag permutacija $Z_n$ ([OEIS A001250](http://oeis.org/A001250)), počevši od $n=0$, iznosi:

$$
1, 1, 2, 4, 10, 32, 122, 544, \cdots
$$

Na primjer, alternirajuće permutacije za prvih nekoliko $n$ jesu:

$$
\begin{aligned}
n=1: & \{1\}\\
n=2: & \{1,2\}, \{2,1\}\\
n=3: & \{1,3,2\}, \{2,1,3\}, \{2,3,1\}, \{3,1,2\}\\
n=4: & \{1,3,2,4\}, \{1,4,2,3\}, \{2,1,4,3\}, \{2,3,1,4\}, \{2,4,1,3\}, \\
& \{3,1,4,2\}, \{3,2,4,1\}, \{3,4,1,2\}, \{4,1,3,2\}, \{4,2,3,1\}
\end{aligned}
$$

## Alternirajuće permutacije i zigzag brojevi

(Pojam treba razlikovati od „deranžmana”.)

Za $n$ veće od $1$ obrat svake zigzag permutacije ponovno je zigzag permutacija, pa ih možemo spariti u parove; stoga je njihov broj nužno paran.

Ovdje dajemo još jedan način sparivanja: zigzag permutacije dijelimo na alternirajuće permutacije (alternating permutation) i obrnuto alternirajuće permutacije (reverse alternating permutation).

Prvi element alternirajuće permutacije veći je od drugoga; odnosi veličina su:

$$
c_1>c_2<c_3>\cdots
$$

Prvi element obrnuto alternirajuće permutacije manji je od drugoga; odnosi veličina su:

$$
c_1<c_2>c_3<\cdots
$$

Zamijenimo li međusobno $1$ i $n$, zatim $2$ i $n-1$ i tako dalje, skup alternirajućih i skup obrnuto alternirajućih permutacija međusobno se zamjenjuju. Stoga je broj alternirajućih permutacija jednak broju obrnuto alternirajućih i iznosi točno polovinu broja zigzag permutacija.

Za $n$ veće od $1$ označimo:

$$
A_n=\frac{Z_n}{2}
$$

Definiramo početne vrijednosti:

$$
A_0=A_1=1
$$

Ovi se $A_n$ nazivaju zigzag brojevima (Euler zigzag number, [OEIS A000111](http://oeis.org/A000111)); počevši od $n=0$, oni iznose:

$$
1, 1, 1, 2, 5, 16, 61, 272, \cdots
$$

Pokušajmo sada izračunati $A_n$.

Od brojeva od $1$ do $n$ odaberemo $k$ brojeva koji tvore podskup; za to postoji $\dbinom{n}{k}$ načina.

U tom $k$-članom podskupu odaberemo obrnuto alternirajuću permutaciju $u$, za što postoji $A_k$ načina; u preostalom podskupu od $n-k$ elemenata, koji dobijemo oduzimanjem tog $k$-članog podskupa od cijelog skupa, odaberemo obrnuto alternirajuću permutaciju $v$, za što postoji $A_{n-k}$ načina.

Razmotrimo permutaciju $w$ od $n+1$ elemenata: na početak stavimo obrnuti $u$, zatim nadovežemo $n+1$, a zatim $v$. Tada je $w$ sigurno zigzag permutacija, a svaka zigzag permutacija od $n+1$ elemenata može se presjeći na mjestu elementa $n+1$ i tako dati odgovarajuće obrnuto alternirajuće permutacije $u$ i $v$, pri čemu različite zigzag permutacije od $n+1$ elemenata daju različite $u$ i $v$.

Stoga vrijedi rekurzivna relacija:

$$
2A_{n+1}=\sum_{k=0}^n \dbinom{n}{k} A_k A_{n-k}
$$

$$
2(n+1)\frac{A_{n+1}}{(n+1)!}=\sum_{k=0}^n \frac{A_k}{k!}\frac{A_{n-k}}{(n-k)!}
$$

Za $n$ jednako $0$ ova rekurzija ne vrijedi; početne vrijednosti $A_0$ i $A_1$ obje su $1$.

Vidimo da je riječ o konvoluciji eksponencijalnih funkcija izvodnica. Pretpostavimo da je eksponencijalna funkcija izvodnica niza $A_n$ jednaka $y$; tada imamo diferencijalnu jednadžbu:

$$
2\frac{\mathrm{d}y}{\mathrm{d}x}=y^2+1
$$

Dodavanje $1$ na desnoj strani jednadžbe služi obradi posebnog slučaja kad je $n$ jednako $0$. Opće rješenje te jednadžbe jest:

$$
y=\tan\left(\frac{1}{2}x+C\right)
$$

Uvrstimo li da je $0$-ti član jednak $1$, dobivamo partikularno rješenje:

$$
y=\tan x+\sec x
$$

Tangens je neparna funkcija, a sekans parna; njihov zbroj tvori funkciju izvodnicu zigzag brojeva.

## Veza Entringerovih brojeva i zigzag brojeva

Prema definiciji Entringerovih brojeva, Entringerov broj $E(n,k)$ broj je alternirajućih permutacija brojeva od $0$ do $n$ čiji je prvi element $k$. Stoga su Entringerovi brojevi i zigzag brojevi zapravo povezani relacijom:

$$
A_n=E(n,n)
$$

Postoji i razlog zašto se $A_n$ nazivaju „zigzag brojevima”: neka je $E_n$ Eulerov broj (Euler number), a $B_n$ Bernoullijev broj.

Za parno $n$ zigzag brojevi s parnim indeksom nazivaju se i „brojevima sekansa” $S_n$ ili „zig brojevima”. Vrijedi relacija:

$$
A_n=(-1)^{n/2}E_n
$$

Prvih nekoliko članova jest ([OEIS A000364](http://oeis.org/A000364)):

$$
1, 1, 5, 61, 1385, \cdots
$$

Za neparno $n$ zigzag brojevi s neparnim indeksom nazivaju se i „brojevima tangensa” $T_n$ ili „zag brojevima”. Vrijedi relacija:

$$
A_n=\frac{(-1)^{(n-1)/2}2^{n+1}(2^{n+1}-1)B_{n+1}}{n+1}
$$

Prvih nekoliko članova jest ([OEIS A000182](http://oeis.org/A000182)):

$$
1, 2, 16, 272, 7936, \cdots
$$

Stoga Taylorov razvoj u točki $x=0$ daje brojeve sekansa i brojeve tangensa:

$$
\sec x=A_0+A_2\frac{x^2}{2!}+A_4\frac{x^4}{4!}+\cdots
$$

$$
\tan x=A_1x+A_3\frac{x^3}{3!}+A_5\frac{x^5}{5!}+\cdots
$$

Ili zapisano zajedno:

$$
\sec x+\tan x=A_0+A_1x+A_2\frac{x^2}{2!}+A_3\frac{x^3}{3!}+A_4\frac{x^4}{4!}+A_5\frac{x^5}{5!}+\cdots
$$

što tvori funkciju izvodnicu zigzag brojeva.

## Literatura i poveznice

1.  [Alternating permutation - Wikipedia](https://en.wikipedia.org/wiki/Alternating_permutation)
