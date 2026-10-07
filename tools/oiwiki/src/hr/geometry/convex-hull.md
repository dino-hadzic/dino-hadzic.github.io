---
title: Konveksna ljuska
---

## Dvodimenzionalna konveksna ljuska

### Definicija

#### Konveksan mnogokut

Konveksan mnogokut je **jednostavan mnogokut** čiji su svi unutarnji kutovi u rasponu $[0,\pi]$.

#### Konveksna ljuska

Najmanji konveksan mnogokut u ravnini koji sadrži sve zadane točke zove se konveksna ljuska (convex hull).

Definicija: za zadani skup $X$, presjek $S$ svih konveksnih skupova koji sadrže $X$ zove se **konveksna ljuska** skupa $X$.

Zapravo je možemo zamisliti kao oblik koji poprimi gumica rastegnuta oko svih zadanih točaka.

Konveksna ljuska obuhvaća sve zadane točke uz najmanji opseg. Ako konkavan mnogokut obuhvaća sve točke, njegov opseg sigurno nije najmanji, kao na slici dolje. Prema nejednakosti trokuta konveksan mnogokut je po opsegu sigurno optimalan.

![](./images/ch.png)

### Andrewov algoritam za konveksnu ljusku

Uobičajeni postupci su Grahamov scan i Andrewov algoritam; ovdje uglavnom predstavljamo Andrewov algoritam.

#### Svojstva

Vremenska složenost algoritma je $O(n\log n)$, gdje je $n$ veličina skupa točaka za koji tražimo ljusku; usko grlo složenosti je sortiranje svih točaka po dvama ključevima.

#### Postupak

Najprije sve točke sortiramo tako da je x-koordinata prvi ključ, a y-koordinata drugi ključ.

Očito su nakon sortiranja najmanji i najveći element sigurno na konveksnoj ljusci. Osim toga, budući da je mnogokut konveksan, ako iz jedne točke krenemo u smjeru suprotnom od kazaljke na satu, putanja uvijek „skreće ulijevo”; čim se pojavi skretanje udesno, taj dio nije na ljusci. Zato gornju i donju ljusku možemo održavati monotonim stogom.

Gledano slijeva nadesno, gornja i donja ljuska zakreću u različitim smjerovima, pa, da bi monotoni stog radio, najprije **uzlaznim nabrajanjem** dobivamo donju ljusku, a zatim **silaznim** gornju ljusku.

Pri računanju ljuske, čim otkrijemo da se smjer kretanja od dviju točaka s vrha stoga ($S_1,S_2$, gdje je $S_1$ vrh) prema točki koja ulazi na stog ($P$) zakreće udesno, tj. da je vektorski produkt manji od $0$: $\overrightarrow{S_2S_1}\times \overrightarrow{S_1P}<0$, izbacujemo vrh stoga, vraćamo se korak natrag i nastavljamo provjeravati dok ne bude $\overrightarrow{S_2S_1}\times \overrightarrow{S_1P}\ge 0$ ili dok na stogu ne ostane samo jedan element.

Obično nije potrebno zadržati točke koje leže na stranicama ljuske, pa se „$<$” u gornjem uvjetu $\overrightarrow{S_2S_1}\times \overrightarrow{S_1P}<0$ po potrebi može zamijeniti s $\le$, a drugi uvjet tada treba promijeniti u $>$.

![Andrew](./images/andrew.svg)

#### Implementacija

???+ note "Implementacija"
    === "C++"
        ```cpp
        // stk[] je cjelobrojan, čuva indekse
        // p[] čuva vektore ili točke
        tp = 0;                       // inicijalizacija stoga
        std::sort(p + 1, p + 1 + n);  // sortiranje točaka
        stk[++tp] = 1;
        // Prvi element stavljamo na stog bez postavljanja used, da bi 1 pri zatvaranju ljuske na kraju također ažurirala monotoni stog
        for (int i = 2; i <= n; ++i) {
          while (tp >= 2  // u sljedećem retku operator * je preopterećen kao vektorski produkt
                 && (p[stk[tp]] - p[stk[tp - 1]]) * (p[i] - p[stk[tp]]) <= 0)
            used[stk[tp--]] = 0;
          used[i] = 1;  // used označava da je točka na ljusci
          stk[++tp] = i;
        }
        int tmp = tp;  // tmp je veličina donje ljuske
        for (int i = n - 1; i > 0; --i)
          if (!used[i]) {
            // ↓pri računanju gornje ljuske ne diramo donju
            while (tp > tmp && (p[stk[tp]] - p[stk[tp - 1]]) * (p[i] - p[stk[tp]]) <= 0)
              used[stk[tp--]] = 0;
            used[i] = 1;
            stk[++tp] = i;
          }
        for (int i = 1; i <= tp; ++i)  // kopiranje u novo polje
          h[i] = p[stk[i]];
        int ans = tp - 1;
        ```
    
    === "Python"
        ```python
        stk = []  # cjelobrojan, čuva indekse
        p = []  # čuva vektore ili točke
        tp = 0  # inicijalizacija stoga
        p.sort()  # sortiranje točaka
        tp = tp + 1
        stk[tp] = 1
        # Prvi element stavljamo na stog bez postavljanja used, da bi 1 pri zatvaranju ljuske na kraju također ažurirala monotoni stog
        for i in range(2, n + 1):
            while tp >= 2 and (p[stk[tp]] - p[stk[tp - 1]]) * (p[i] - p[stk[tp]]) <= 0:
                # u sljedećem retku operator * je preopterećen kao vektorski produkt
                used[stk[tp]] = 0
                tp = tp - 1
            used[i] = 1  # used označava da je točka na ljusci
            tp = tp + 1
            stk[tp] = i
        tmp = tp  # tmp je veličina donje ljuske
        for i in range(n - 1, 0, -1):
            if used[i] == False:
                #      ↓pri računanju gornje ljuske ne diramo donju
                while tp > tmp and (p[stk[tp]] - p[stk[tp - 1]]) * (p[i] - p[stk[tp]]) <= 0:
                    used[stk[tp]] = 0
                    tp = tp - 1
                used[i] = 1
                tp = tp + 1
                stk[tp] = i
        for i in range(1, tp + 1):
            h[i] = p[stk[i]]
        ans = tp - 1
        ```

Prema gornjem kodu na kraju je na ljusci $\textit{ans}$ elemenata (točka $1$ pohranjena je dodatno, pa polje $h$ ima $\textit{ans}+1$ elemenata), poredanih u smjeru suprotnom od kazaljke na satu. Opseg je

$$
\sum_{i=1}^{\textit{ans}}\left|\overrightarrow{h_ih_{i+1}}\right|
$$

### Grahamov scan

#### Svojstva

Kao i Andrewov algoritam, Grahamov scan ima vremensku složenost $O(n\log n)$, a usko grlo je također sortiranje svih točaka.

#### Postupak

Najprije među svim točkama pronađemo točku $P$ s najmanjom y-koordinatom. Prema definiciji konveksne ljuske znamo da je ta točka sigurno na ljusci. Zatim sve točke sortiramo po polarnom kutu u odnosu na točku $P$.

![](./images/ch1.svg)

Slično kao kod Andrewova algoritma, ako iz točke $P$ krenemo po ljusci u smjeru suprotnom od kazaljke na satu, sve točke kroz koje prolazimo sigurno „skreću ulijevo”. Formalno, za bilo koje tri uzastopne točke $P_1, P_2, P_3$ na ljusci u smjeru suprotnom od kazaljke na satu vrijedi $\overrightarrow{P_1 P_2} \times \overrightarrow{P_2 P_3} \ge 0$.

Napravimo stog za pohranu ljuske, najprije na njega stavimo $P$, a zatim po polarnom kutu redom pokušavamo dodati svaku točku. Ako smjer kretanja od dviju točaka s vrha stoga $P_1, P_2$ (gdje je $P_1$ vrh) prema točki $P_0$ koja ulazi na stog „skreće udesno”, izbacujemo vrh $P_1$ i to ponavljamo dok točka koja ulazi i dvije točke s vrha stoga ne zadovolje uvjet ili dok na stogu ne ostane samo jedan element, a zatim stavimo $P_0$ na stog.

![](./images/ch2.svg)

![](./images/ch3.svg)

???+ note "Implementacija"
    ```cpp
    struct Point {
      double x, y, ang;
    
      Point operator-(const Point& p) const { return {x - p.x, y - p.y, 0}; }
    } p[MAXN];
    
    double dis(Point p1, Point p2) {
      return sqrt((p1.x - p2.x) * (p1.x - p2.x) + (p1.y - p2.y) * (p1.y - p2.y));
    }
    
    bool cmp(Point p1, Point p2) {
      if (p1.ang == p2.ang) {
        return dis(p1, p[1]) < dis(p2, p[1]);
      }
      return p1.ang < p2.ang;
    }
    
    double cross(Point p1, Point p2) { return p1.x * p2.y - p1.y * p2.x; }
    
    int main() {
      for (int i = 2; i <= n; ++i) {
        if (p[i].y < p[1].y || (p[i].y == p[1].y && p[i].x < p[1].x)) {
          std::swap(p[1], p[i]);
        }
      }
      for (int i = 2; i <= n; ++i) {
        p[i].ang = atan2(p[i].y - p[1].y, p[i].x - p[1].x);
      }
      std::sort(p + 2, p + n + 1, cmp);
      sta[++top] = 1;
      for (int i = 2; i <= n; ++i) {
        while (top >= 2 &&
               cross(p[sta[top]] - p[sta[top - 1]], p[i] - p[sta[top]]) < 0) {
          top--;
        }
        sta[++top] = i;
      }
      return 0;
    }
    ```

## Suma Minkowskog

### Definicija

Suma Minkowskog $P+Q$ skupova točaka $P$ i $Q$ definira se kao $P+Q=\{a+b|a\in P,b\in Q\}$: svaku točku skupa $Q$ gledamo kao vektor, svaku točku skupa $P$ translatiramo za te vektore i skup svih dobivenih točaka je $P+Q$. Ovdje razmatramo samo sumu Minkowskog **konveksnih ljuski**.

Na primjer, za skup točaka $P=\{(0,0),(-3,3),(2,1)\}$ i skup točaka $Q=\{(0,0),(-1,3),(1,4),(2,2)\}$:

![](./images/convex-hull1.svg)

Translatiramo $P$ za svaki vektor iz $Q$:

![](./images/convex-hull2.svg)

Lako je uočiti da je novi lik također **konveksna ljuska**:

![](./images/convex-hull3.svg)

### Svojstva

1.  Ako su skupovi točaka $P$ i $Q$ konveksni, i njihova suma Minkowskog $P+Q$ je konveksan skup.

    ??? note "Dokaz"
        Neka su $e,f\in P+Q$; postoje $a,b \in P$ i $c,d\in Q$ takvi da je $e=a+c,f=b+d$. Tada za svaki $t\in[0,1]$ vrijedi:
        
        $$
        \begin{aligned}
        te + (1-t)f &= t(a+c)+(1-t)(b+d)\\
        &=(ta+(1-t)b)+(tc+(1-t)d)\\
        &\in P+Q.
        \end{aligned}
        $$
        
        Time je dokaz završen.
2.  Ako su skupovi točaka $P$ i $Q$ konveksni, skup stranica njihove sume Minkowskog $P+Q$ dobiva se tako da stranice konveksnih skupova $P$ i $Q$ sortiramo po polarnom kutu i nadovežemo.

    ??? note "Dokaz"
        Bez smanjenja općenitosti pretpostavimo da nijedna stranica konveksnog skupa $P$ nema isti nagib kao neka stranica skupa $Q$. Zarotirajmo koordinatni sustav tako da je neka stranica $XY$ skupa $P$ paralelna s osi $x$ i da je najniža.
        
        Neka je tada $U$ najniža točka skupa $Q$, a $A$ **najniža** i **najljevija** točka skupa $P+Q$.
        
        Vidimo da je $\vec{A} = \vec{X} + \vec{U}$, pa $A$ nužno leži na rubu skupa $P+Q$.
        
        Slično, za **najnižu** i **najdesniju** točku $B$ skupa $P+Q$ vrijedi $\vec{B} = \vec{Y} + \vec{U}$, pa i ona nužno leži na rubu skupa $P+Q$.
        
        Stoga je $\vec{AB} = \vec{XY} + \vec{U}$.
        
        Ako rotacije izvodimo redom, rezultati uzastopno čine svaku stranicu skupa $P+Q$.
        
        Time je dokaz završen.

### Implementacija

Prema svojstvu 2 možemo konveksne skupove $P,Q$ sortirati po polarnom kutu i tako dobiti redoslijed kojim se njihove stranice pojavljuju na $P+Q$; točku $P_1+Q_1$ uzmemo kao početak skupa $P+Q$ i zatim stranice redom dodajemo postupkom sličnim **spajanju (merge)**.

Vremenska složenost: $O(n+m)$

???+ note "Implementacija"
    ```cpp
    template <class T>
    struct Point {
      T x, y;
    
      Point(T x = 0, T y = 0) : x(x), y(y) {}
    
      friend Point operator+(const Point &a, const Point &b) {
        return {a.x + b.x, a.y + b.y};
      }
    
      friend Point operator-(const Point &a, const Point &b) {
        return {a.x - b.x, a.y - b.y};
      }
    
      // Skalarni produkt
      friend T operator*(const Point &a, const Point &b) {
        return a.x * b.x + a.y * b.y;
      }
    
      // Vektorski produkt
      friend T operator^(const Point &a, const Point &b) {
        return a.x * b.y - a.y * b.x;
      }
    };
    
    template <class T>
    vector<Point<T>> minkowski_sum(vector<Point<T>> a, vector<Point<T>> b) {
      vector<Point<T>> c{a[0] + b[0]};
      for (usz i = 0; i + 1 < a.size(); ++i) a[i] = a[i + 1] - a[i];
      for (usz i = 0; i + 1 < b.size(); ++i) b[i] = b[i + 1] - b[i];
      a.pop_back(), b.pop_back();
      c.resize(a.size() + b.size() + 1);
      merge(a.begin(), a.end(), b.begin(), b.end(), c.begin() + 1,
            [](const Point<T> &a, const Point<T> &b) { return (a ^ b) < 0; });
      for (usz i = 1; i < c.size(); ++i) c[i] = c[i] + c[i - 1];
      return c;
    }
    ```

### Primjer

???+ note "[Primjer: \[JSOI2018\] Rat](https://loj.ac/p/2549)"
    Zadane su dvije konveksne ljuske $P,Q$; ljuska $Q$ se translatira $q$ puta i nakon svakog pomaka treba odgovoriti sijeku li se. $1\le n,m\le 10^5,1\le q\le 10^5$.

??? note "Implementacija"
    ```cpp
    --8<-- "docs/geometry/code/convex-hull/convex-hull_1.cpp"
    ```

## Trodimenzionalna konveksna ljuska

### Osnovni pojmovi

> Inverzija s obzirom na kružnicu: neka je $O$ središte inverzije, a $R$ polumjer inverzije. Ako pravac kroz $O$ prolazi točkama $P$ i $P'$ i vrijedi $OP\times OP'=R^{2}$, kažemo da su $P$ i $P'$ međusobno inverzne s obzirom na $O$.

### Postupak

Postupak računanja ljuske:

-   Najprije točke malo perturbiramo da izbjegnemo slučaj četiriju komplanarnih točaka.
-   Za već poznatu ljusku dodajemo novu točku $P$; $P$ gledamo kao točkasti izvor svjetlosti koji baca zrake na ljusku. Vidljive i nevidljive strane sigurno su odvojene nizom bridova.
-   Vidljive strane brišemo i dodajemo strane koje čine ti granični bridovi i $P$.
    Ponavljamo postupak; prema [Pickovu teoremu](./pick.md), Eulerovoj formuli (za konveksan poliedar broj vrhova $V$, bridova $E$ i strana $F$ zadovoljava $V−E+F=2$) i inverziji s obzirom na kružnicu, složenost je $O(n^2)$.[^3d-v]

### Zadatak-predložak

[P4724 [Predložak] Trodimenzionalna konveksna ljuska](https://www.luogu.com.cn/problem/P4724)

Ponavljanjem gornjeg postupka dobivamo rješenje.

???+ note "Implementacija"
    ```cpp
    --8<-- "docs/geometry/code/3d/3d_1.cpp"
    ```

## Zadaci za vježbu

-   [UVa11626 Convex Hull](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=78&page=show_problem&problem=2673)

-   [„USACO5.1” Fencing the Cows](https://www.luogu.com.cn/problem/P2742)

-   [POJ1873 The Fortified Forest](http://poj.org/problem?id=1873)

-   [POJ1113 Wall](http://poj.org/problem?id=1113)

-   [USACO22JAN Multiple Choice Test P](https://www.luogu.com.cn/problem/P8101)

-   [„SHOI2012” Konveksna ljuska kreditnih kartica](https://www.luogu.com.cn/problem/P3829)

## Literatura i napomene

[^3d-v]: [Bilješke o učenju trodimenzionalne konveksne ljuske](https://www.cnblogs.com/xzyxzy/p/10225804.html)
