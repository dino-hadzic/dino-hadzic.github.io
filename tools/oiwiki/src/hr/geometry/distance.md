---
title: Udaljenost
---

## Euklidska udaljenost

### Dvodimenzionalni prostor

#### Definicija

Euklidska udaljenost. U pravokutnom koordinatnom sustavu, ako su koordinate točaka $A,B$ redom $A(x_1,y_1),B(x_2,y_2)$, euklidska udaljenost između njih je:

$$
\left | AB \right | = \sqrt{\left ( x_2 - x_1 \right )^2 + \left ( y_2 - y_1 \right )^2}
$$

#### Objašnjenje

Na primjer, ako su u pravokutnom koordinatnom sustavu zadane točke $A(6,5),B(2,2)$, formulom lako dobivamo euklidsku udaljenost između $A$ i $B$:

$$
\left | AB \right | = \sqrt{\left ( 2 - 6 \right )^2 + \left ( 2 - 5 \right )^2} = \sqrt{4^2+3^2} = 5
$$

Osim toga, euklidska udaljenost točke $P(x,y)$ od ishodišta može se izraziti formulom:

$$
|P| = \sqrt{x^2+y^2}
$$

### n-dimenzionalni prostor

#### Uvod

A kako glasi formula za euklidsku udaljenost dviju točaka u trodimenzionalnom prostoru? Promotrimo sliku.

![dis-3-dimensional](./images/distance-0.png)

Lako uočavamo da je u $\triangle ADC$ kut $\angle ADC = 90^\circ$, a u $\triangle ACB$ kut $\angle ACB = 90^\circ$.

$$
\begin{aligned}
\therefore ~ |AB| &= \sqrt{|AC|^2+|BC|^2} \\
&= \sqrt{|AD|^2+|CD|^2+|BC|^2}
\end{aligned}
$$

#### Definicija

Odatle slijedi formula za euklidsku udaljenost u trodimenzionalnom prostoru:

$$
\begin{gathered}
\left | AB \right | = \sqrt{\left ( x_2 - x_1 \right )^2 + \left ( y_2 - y_1 \right )^2 + \left ( z_2 - z_1 \right )^2} \\
|P| = \sqrt{x^2+y^2+z^2}
\end{gathered}
$$

#### Objašnjenje

Zadatak [NOIP2017 Sir](https://uoj.ac/problem/332) koristi ovo znanje i može poslužiti kao primjer za euklidsku udaljenost.

Analogno dobivamo formulu za euklidsku udaljenost u $n$-dimenzionalnom prostoru: za $\vec A(x_{11}, x_{12}, \cdots,x_{1n}) ,~ \vec B(x_{21}, x_{22}, \cdots,x_{2n})$ vrijedi

$$
\begin{aligned}
\lVert\overrightarrow{AB}\rVert &= \sqrt{\left ( x_{11} - x_{21} \right )^2 + \left ( x_{12} - x_{22} \right )^2 + \cdot \cdot \cdot +\left ( x_{1n} - x_{2n} \right )^2}\\
&= \sqrt{\sum_{i = 1}^{n}(x_{1i} - x_{2i})^2}
\end{aligned}
$$

Iako je euklidska udaljenost vrlo korisna, ima i očit nedostatak. Pri računanju euklidske udaljenosti dviju cjelobrojnih točaka rezultat je često broj s pomičnim zarezom, pa postoji određena pogreška.

## Manhattanska udaljenost

### Definicija

U dvodimenzionalnom prostoru manhattanska udaljenost (Manhattan distance) između dviju točaka jednaka je zbroju apsolutne vrijednosti razlike apscisa i apsolutne vrijednosti razlike ordinata. Za točke $A(x_1,y_1),B(x_2,y_2)$ manhattanska udaljenost između $A$ i $B$ izražava se formulom:

$$
d(A,B) = |x_1 - x_2| + |y_1 - y_2|
$$

### Objašnjenje

Promotrimo sliku:

![manhattan-dis-diff](./images/distance-1.png)

Između $A$ i $B$ žuta i narančasta linija prikazuju manhattansku udaljenost, crvena i plava linija prikazuju ekvivalentne manhattanske udaljenosti, a zelena linija prikazuje euklidsku udaljenost.

Isti primjer: na slici ispod koordinate točaka $A,B$ su $A(25,20),B(10,10)$.

![manhattan-dis](./images/distance-2.svg)

Formulom lako dobivamo manhattansku udaljenost između $A$ i $B$:

$$
d(A,B) = |20 - 10| + |25 - 10| = 10 + 15 = 25
$$

Izvođenjem dobivamo formulu za manhattansku udaljenost u $n$-dimenzionalnom prostoru:

$$
\begin{aligned}
d(A,B) &= |x_1 - y_1| + |x_2 - y_2| + \cdot \cdot \cdot + |x_n - y_n|\\
&= \sum_{i = 1}^{n}|x_i - y_i|
\end{aligned}
$$

### Svojstva

Osim formule, manhattanska udaljenost ima i sljedeća matematička svojstva:

-   Nenegativnost: manhattanska udaljenost je nenegativan broj, tj. $d(i,j)\geq 0$.
-   Identitet: manhattanska udaljenost točke od same sebe jednaka je $0$, tj. $d(i,i) = 0$.
-   Simetričnost: manhattanska udaljenost od $A$ do $B$ jednaka je onoj od $B$ do $A$, tj. $d(i,j) = d(j,i)$.
-   Nejednakost trokuta: izravna udaljenost od točke $i$ do $j$ nije veća od udaljenosti preko bilo koje druge točke $k$, tj. $d(i,j)\leq d(i,k)+d(k,j)$.

### Primjer zadatka

[P5098 „USACO04OPEN” Cave Cows 3](https://www.luogu.com.cn/problem/P5098)

Prema zadatku, za izraz $|x_1-x_2|+|y_1-y_2|$ možemo pretpostaviti $x_1 - x_2 \geq 0$ i prema predznaku $y_1 - y_2$ razlikovati dva slučaja:

-   $(y_1 - y_2 \geq 0)\rightarrow |x_1-x_2|+|y_1-y_2|=x_1 + y_1 - (x_2 + y_2)$

-   $(y_1 - y_2 < 0)\rightarrow |x_1-x_2|+|y_1-y_2|=x_1 - y_1 - (x_2 - y_2)$

Dovoljno je izračunati maksimum i minimum od $x+y$ i $x-y$ da bismo dobili odgovor.

??? note "Referentni kôd"
    === "C++"
        ```cpp
        #include <algorithm>
        #include <cstdio>
        using namespace std;
        
        int main() {
          int n, x, y, minx = 0x7fffffff, maxx = 0, miny = 0x7fffffff, maxy = 0;
          scanf("%d", &n);
          for (int i = 1; i <= n; i++) {
            scanf("%d%d", &x, &y);
            minx = min(minx, x + y), maxx = max(maxx, x + y);
            miny = min(miny, x - y), maxy = max(maxy, x - y);
          }
          printf("%d\n", max(maxx - minx, maxy - miny));
          return 0;
        }
        ```
    
    === "Python"
        ```python
        minx = 0x7FFFFFFF
        maxx = 0
        miny = 0x7FFFFFFF
        maxy = 0
        n = int(input())
        for i in range(1, n + 1):
            x, y = map(lambda x: int(x), input().split())
            minx = min(minx, x + y)
            maxx = max(maxx, x + y)
            miny = min(miny, x - y)
            maxy = max(maxy, x - y)
        print(max(maxx - minx, maxy - miny))
        ```

Postoji i drugi pristup: manhattansku udaljenost pretvoriti u Čebiševljevu, o čemu govori posljednji dio.

## Čebiševljeva udaljenost

### Definicija

Čebiševljeva udaljenost (Chebyshev distance) metrika je u vektorskom prostoru u kojoj je udaljenost dviju točaka definirana kao maksimum apsolutnih razlika njihovih koordinata.[^ref1]

U dvodimenzionalnom prostoru Čebiševljeva udaljenost između dviju točaka jednaka je maksimumu apsolutne vrijednosti razlike apscisa i apsolutne vrijednosti razlike ordinata. Za točke $A(x_1,y_1),B(x_2,y_2)$ Čebiševljeva udaljenost između $A$ i $B$ izražava se formulom:

$$
d(A,B) = \max(|x_1 - x_2|, |y_1 - y_2|)
$$

Formula za Čebiševljevu udaljenost u $n$-dimenzionalnom prostoru glasi:

$$
\begin{aligned}
d(x,y) &= \max\begin{Bmatrix} |x_1 - y_1|,|x_2 - y_2|,\cdot \cdot \cdot,|x_n - y_n|\end{Bmatrix} \\
&= \max\begin{Bmatrix} |x_i - y_i|\end{Bmatrix}(i \in [1, n])\end{aligned}
$$

### Objašnjenje

Opet isti primjer: na slici ispod koordinate točaka $A,B$ su $A(25,20),B(10,10)$.

![Chebyshev-dis](./images/distance-2.svg)

$$
d(A,B) = \max(|20 - 10|, |25 - 10|) = \max(10, 15) = 15
$$

## Pretvorba između manhattanske i Čebiševljeve udaljenosti

### Postupak

Najprije nacrtajmo u pravokutnom koordinatnom sustavu sve točke čija je manhattanska udaljenost od ishodišta jednaka $1$.

Iz formule lako dobivamo jednadžbu $|x| + |y| = 1$.

Raspisivanjem apsolutnih vrijednosti dobivamo $4$ linearne funkcije:

$$
\begin{aligned}
&y = -x + 1 &(x \geq 0, y \geq 0) \\
&y = x + 1 &(x \leq 0, y \geq 0) \\
&y = x - 1  &(x \geq 0, y \leq 0)  \\
&y = -x - 1  &(x \leq 0, y \leq 0) \\
\end{aligned}
$$

Nacrtamo li te $4$ funkcije u koordinatnom sustavu, dobivamo kvadrat sa stranicom $\sqrt{2}$, kao na slici:

![dis-diff-square-1](./images/distance-3.svg)

Sve točke na rubu kvadrata imaju manhattansku udaljenost $1$ od ishodišta.

Analogno nacrtajmo sve točke čija je Čebiševljeva udaljenost od ishodišta jednaka $1$.

Iz formule znamo $\max(|x|,|y|)=1$.

Raspisivanjem također dobivamo $4$ dužine:

$$
\begin{aligned}
&y = 1&(-1\leq x \leq 1) \\
&y = -1&(-1\leq x \leq 1) \\
&x = 1,&(-1\leq y \leq 1) \\
&x = -1,&(-1\leq y \leq 1) \\
\end{aligned}
$$

Nacrtane u koordinatnom sustavu daju kvadrat sa stranicom $2$, kao na slici:

![dis-diff-square-2](./images/distance-4.svg)

Sve točke na rubu kvadrata imaju Čebiševljevu udaljenost $1$ od ishodišta.

Usporedimo li ove dvije slike, iznenađujuće otkrivamo:

ta su $2$ kvadrata slični likovi.

### Dokaz

Postoji li, dakle, veza između manhattanske i Čebiševljeve udaljenosti?

Dokažimo to ukratko:

Neka su $A(x_1,y_1),B(x_2,y_2)$.

Raspišemo li apsolutne vrijednosti u manhattanskoj udaljenosti, dobivamo četiri vrijednosti; najveća od njih zbroj je dvaju nenegativnih brojeva, tj. manhattanska udaljenost. Manhattanska udaljenost točaka $A,B$ tada je:

$$
\begin{aligned}
d(A,B)&=|x_1 - x_2| + |y_1 - y_2|\\
&=\max\begin{Bmatrix} x_1 - x_2 + y_1 - y_2, x_1 - x_2 + y_2 - y_1,x_2 - x_1 + y_1 - y_2, x_2 - x_1 + y_2 - y_1\end{Bmatrix}\\
&= \max(|(x_1 + y_1) - (x_2 + y_2)|, |(x_1 - y_1) - (x_2 - y_2)|)
\end{aligned}
$$

Lako uočavamo da je to Čebiševljeva udaljenost između točaka $(x_1 + y_1,x_1 - y_1), (x_2 + y_2,x_2 - y_2)$.

Dakle, pretvorimo li svaku točku $(x,y)$ u $(x + y, x - y)$, Čebiševljeva udaljenost u novom koordinatnom sustavu jednaka je manhattanskoj udaljenosti u izvornom.

Analogno, Čebiševljeva udaljenost točaka $A,B$ je:

$$
\begin{aligned}
d(A,B)&=\max\begin{Bmatrix} |x_1 - x_2|,|y_1 - y_2|\end{Bmatrix}\\
&=\max\begin{Bmatrix} \left|\dfrac{x_1 + y_1}{2}-\dfrac{x_2 + y_2}{2}\right|+\left|\dfrac{x_1 - y_1}{2}-\dfrac{x_2 - y_2}{2}\right|\end{Bmatrix}
\end{aligned}
$$

A to je manhattanska udaljenost između točaka $(\dfrac{x_1 + y_1}{2},\dfrac{x_1 - y_1}{2}), (\dfrac{x_2 + y_2}{2},\dfrac{x_2 - y_2}{2})$.

Dakle, pretvorimo li svaku točku $(x,y)$ u $(\dfrac{x + y}{2},\dfrac{x - y}{2})$, manhattanska udaljenost u novom koordinatnom sustavu jednaka je Čebiševljevoj udaljenosti u izvornom.

### Zaključak

-   Manhattanski koordinatni sustav dobiva se rotacijom Čebiševljeva koordinatnog sustava za $45^\circ$ i smanjenjem na polovinu.
-   Pretvorimo li koordinate točke $(x,y)$ u $(x + y, x - y)$, manhattanska udaljenost u izvornom sustavu jednaka je Čebiševljevoj udaljenosti u novom.
-   Pretvorimo li koordinate točke $(x,y)$ u $(\dfrac{x + y}{2},\dfrac{x - y}{2})$, Čebiševljeva udaljenost u izvornom sustavu jednaka je manhattanskoj udaljenosti u novom.

Kad naiđemo na zadatak s Čebiševljevom ili manhattanskom udaljenošću, često ih možemo međusobno pretvarati. Obje udaljenosti imaju svoje prednosti i nedostatke u različitim zadacima i treba ih fleksibilno koristiti.

### Primjeri zadataka

[P4648 „IOI2007” pairs Parovi životinja](https://www.luogu.com.cn/problem/P4648) (manhattanska u Čebiševljevu)

[P3964 „TJOI2013” Okupljanje vjeverica](https://www.luogu.com.cn/problem/P3964) (Čebiševljeva u manhattansku)

Na kraju dajemo drugo rješenje zadatka [P5098 „USACO04OPEN” Cave Cows 3](https://www.luogu.com.cn/problem/P5098):

Manhattansku udaljenost iz zadatka pretvorimo u Čebiševljevu, tj. koordinate svake točke $(x,y)$ zamijenimo s $(x + y, x - y)$.

Traženi odgovor postaje $\max\limits_{i,j\in n}\begin{Bmatrix} \max\begin{Bmatrix} |x_i - x_j|,|y_i - y_j|\end{Bmatrix}\end{Bmatrix}$.

Da bi razlika apscisa i razlika ordinata bile najveće, dovoljno je unaprijed izračunati maksimum i minimum od $x,y$.

??? note "Referentni kôd"
    === "C++"
        ```cpp
        #include <algorithm>
        #include <cstdio>
        using namespace std;
        
        int main() {
          int n, x, y, a, b, minx = 0x7fffffff, maxx = 0, miny = 0x7fffffff, maxy = 0;
          scanf("%d", &n);
          for (int i = 1; i <= n; i++) {
            scanf("%d%d", &a, &b);
            x = a + b, y = a - b;
            minx = min(minx, x), maxx = max(maxx, x);
            miny = min(miny, y), maxy = max(maxy, y);
          }
          printf("%d\n", max(maxx - minx, maxy - miny));
          return 0;
        }
        ```
    
    === "Python"
        ```python
        minx = 0x7FFFFFFF
        maxx = 0
        miny = 0x7FFFFFFF
        maxy = 0
        n = int(input())
        for i in range(1, n + 1):
            a, b = map(lambda x: int(x), input().split())
            x = a + b
            y = a - b
            minx = min(minx, x)
            maxx = max(maxx, x)
            miny = min(miny, y)
            maxy = max(maxy, y)
        print(max(maxx - minx, maxy - miny))
        ```

Usporedimo li ova dva kôda, opet otkrivamo da dva različita pristupa daju potpuno ekvivalentan kôd — zar nije zanimljivo? Naravno, dublje teme ostavljamo za samostalno istraživanje.

## Minkowskijeva udaljenost

Minkowskijevu udaljenost dviju točaka $X(x_1, x_2, \dots, x_n)$, $Y(y_1, y_2, \dots, y_n)$ u $n$-dimenzionalnom prostoru definiramo kao:

$$
D(X, Y) = \left(\sum_{i=1}^n \left\vert x_i - y_i \right\vert ^p\right)^{\frac{1}{p}}.
$$

Posebno:

1.  za $p=1$, $D(X, Y) = \sum_{i=1}^n \left\vert x_i - y_i \right\vert$ je manhattanska udaljenost;
2.  za $p=2$, $D(X, Y) = \left(\sum_{i=1}^n (x_i - y_i)^2\right)^{1/2}$ je euklidska udaljenost;
3.  za $p \to \infty$, $D(X, Y) = \lim_{p \to \infty}\left(\sum_{i=1}^n \left\vert x_i - y_i \right\vert ^p\right) ^{1/p} = \max\limits_{i=1}^n \left\vert x_i - y_i \right\vert$ je Čebiševljeva udaljenost.

Napomena: Minkowskijeva udaljenost je metrika samo za $p \ge 1$; dokaz vidi u [Minkowski distance - Wikipedia](https://en.wikipedia.org/wiki/Minkowski_distance).

## Literatura i poveznice

1.  [Kratko o tri uobičajene udaljenosti](https://www.luogu.com.cn/blog/xuxing/Distance-Algorithm), zahvaljujemo autoru xuxing na dopuštenju.

[^ref1]: [Chebyshev distance - Wikipedia](https://en.wikipedia.org/wiki/Chebyshev_distance)
