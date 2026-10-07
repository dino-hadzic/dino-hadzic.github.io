---
title: Shell sort
---

Ova stranica kratko predstavlja Shell sort.

## Definicija

**Shell sort**, poznat i kao sortiranje sa smanjujućim razmakom (diminishing increment sort), poboljšana je inačica [insertion sorta](./insertion-sort.md). Nazvan je po svom izumitelju Donaldu Shellu.

## Postupak

Sortiranje uspoređuje i premješta zapise koji nisu susjedni:

1.  niz koji sortiramo podijeli se na više podnizova (elementi svakog podniza u izvornom su nizu na jednakom razmaku);
2.  ti se podnizovi sortiraju insertion sortom;
3.  razmak između elemenata podnizova se smanjuje i postupak se ponavlja dok razmak ne padne na $1$.

Radi lakše analize, u nastavku je pseudokod jednog prolaza insertion sorta s razmakom $h$, označenog $\text{InsertionSort}(h)$. Indeksi niza $A$ idu od $1$ do $n$, a $v$ čuva vrijednost koju trenutno umećemo; Shell sort poziva taj postupak za razmake od najvećeg prema najmanjem.

$$
\begin{array}{ll}
1 & \textbf{for } j\gets h+1 \textbf{ to } n\\
2 & \qquad v\gets A_j\\
3 & \qquad i\gets j-h\\
4 & \qquad \textbf{while } i\ge 1 \textbf{ and } A_i>v\\
5 & \qquad\qquad A_{i+h}\gets A_i\\
6 & \qquad\qquad i\gets i-h\\
7 & \qquad A_{i+h}\gets v
\end{array}
$$

## Svojstva

### Stabilnost

Shell sort je nestabilan algoritam sortiranja.

### Vremenska složenost

Najbolje vrijeme Shell sorta ovisi o nizu razmaka i o tome prekida li se ranije; implementacija s razmacima $3h+1$ bez ranog prekida, dana u nastavku, u najboljem slučaju ima $\Theta(n\log n)$.

Prosječna i najgora vremenska složenost Shell sorta ovise o izboru niza razmaka. Neka je niz razmaka $H$; u nastavku su dva klasična izbora $H$, a oba spuštaju složenost sortiranja na razinu $o(n^2)$.

???+ note "Tvrdnja 1"
    Ako je niz razmaka $H= \{ 2^k-1\mid k=1,2,\ldots,\lfloor\log_2 n\rfloor \}$ (od najvećeg prema najmanjem), vremenska složenost Shell sorta je $O(n^{3/2})$.

???+ note "Tvrdnja 2"
    Ako je niz razmaka $H= \{ k=2^p\cdot 3^q\mid p,q\in \mathbb N,k\le n \}$ (od najvećeg prema najmanjem), vremenska složenost Shell sorta je $O(n\log^2 n)$.

Da bismo dokazali te dvije tvrdnje, najprije iskazujemo i dokazujemo važan teorem koji odražava glavno obilježje Shell sorta.

???+ note "Teorem 1"
    Čim program jednom izvrši $\text{InsertionSort}(h)$, bez obzira na to kako se poslije poziva funkcija $\text{InsertionSort}$ i kako se niz $A$ mijenja, svaki od sljedećih podnizova ostaje sortiran:
    
    $$
    \begin{array}{c}
    A_1,A_{1+h},A_{1+2h},\ldots \\
    A_2,A_{2+h},A_{2+2h},\ldots \\
    \vdots \\
    A_h,A_{h+h},A_{h+2h},\ldots
    \end{array}
    $$

Dokažimo teorem 1.

Najprije dokazujemo lemu 1.

???+ note "Lema 1"
    Neka su $n,m$ nenegativni cijeli brojevi, $l$ pozitivan cijeli broj, a $X(x_1,x_2,\ldots,x_{n+l})$ i $Y(y_1,y_2,\ldots,y_{m+l})$ dva niza koja zadovoljavaju:
    
    $$
    y_1 \le x_{n+1},y_2 \le x_{n+2},\ldots,y_l \le x_{n+l}
    $$
    
    Tada, sortiramo li oba niza uzlazno, gornji uvjet i dalje vrijedi.

??? note "Dokaz leme 1"
    Neka je sortirani niz $X$ niz $X'(x'_1,\ldots,x'_{n+l})$, a sortirani niz $Y$ niz $Y'(y'_1,\ldots,y'_{m+l})$.
    
    Za svaki $1\le i\le l$, u $X$ postoji najviše $l-i$ elemenata strogo većih od $x'_{n+i}$. Zato je među odabranih $l$ elemenata $\{x_{n+1},\ldots,x_{n+l}\}$ barem $i$ njih koji nisu veći od $x'_{n+i}$. Označimo ih $x_{n+k_1},\ldots,x_{n+k_i}$; zajedno s izvornim uparenim nejednakostima dobivamo:
    
    $$
    y_{k_1}\le x_{n+k_1}\le x'_{n+i},y_{k_2}\le x_{n+k_2}\le x'_{n+i},\ldots,y_{k_i}\le x_{n+k_i}\le x'_{n+i}
    $$
    
    Dakle $x'_{n+i}$ je veći ili jednak od barem $i$ elemenata niza $Y$, tj. niza $Y'$, pa prirodno vrijedi $y'_i\le x'_{n+i}\,(1\le i\le l)$.

Vratimo se dokazu izvorne tvrdnje. Neka je duljina niza $N$. Dovoljno je dokazati da $\text{InsertionSort}(k)$ čuva postojeću $h$-sortiranost, a zatim indukcijom po broju poziva. Ovdje su $h,k$ proizvoljni pozitivni cijeli brojevi. Ako je $h\ge N$, nema parova elemenata na razmaku $h$ koje bi trebalo provjeriti, pa tvrdnja očito vrijedi. U nastavku pretpostavljamo $h<N$.

Označimo niz prije poziva s $A$, a poslije poziva s $A'$. Prije poziva vrijedi $A_i\le A_{i+h}$ za $1\le i\le N-h$. Za svaki $1\le w\le\min(k,N-h)$ zapišimo dijeljenjem s ostatkom

$$
w+h=v+tk,\qquad 1\le v\le k,\quad t\ge0.
$$

Promotrimo dva potpuna podniza s razmakom $k$ koji počinju na indeksima $w$ i $v$:

$$
Y=(A_w,A_{w+k},A_{w+2k},\ldots),\qquad
X=(A_v,A_{v+k},A_{v+2k},\ldots).
$$

Neka postoji točno $l$ nenegativnih cijelih brojeva $j$ za koje je $w+h+jk\le N$. Tada $X$ ima duljinu $t+l$, a $Y$ duljinu barem $l$; iz postojeće $h$-sortiranosti prvih $l$ članova niza $Y$ i posljednjih $l$ članova niza $X$ zadovoljavaju

$$
y_{j+1}=A_{w+jk}\le A_{w+h+jk}=x_{t+j+1},\qquad 0\le j<l.
$$

$\text{InsertionSort}(k)$ upravo uzlazno sortira svaki takav potpuni podniz. Po lemi 1, nakon sortiranja odgovarajući odnos i dalje vrijedi, tj.

$$
A'_{w+jk}\le A'_{w+h+jk},\qquad 0\le j<l.
$$

Lema vrijedi i kad je $v=w$ i dva su podniza zapravo isti. Svaki se indeks $1\le i\le N-h$ može jedinstveno zapisati kao $i=w+jk$ s $1\le w\le k$, $j\ge0$, pri čemu nužno $w\le N-h$. Dakle gornje razmatranje pokriva sve $i$ i daje $A'_i\le A'_{i+h}$, pa je $h$-sortiranost očuvana i teorem 1 je dokazan.

Taj teorem otkriva ključ zbog kojeg Shell sort s posebnim skupom $H$ može imati bolju složenost: tijekom cijelog postupka čuva se sortiranost prije obrađenih podnizova, pa se u kasnijim pozivima broj pomaka pokazivača $i$ znatno smanjuje.

Zatim izdvajamo i dokazujemo jednu lemu iz teorije brojeva. Taj je teorem u OI zajednici postao vrlo poznat zbog zadatka [Luogu P3951 Xiao Kai's Puzzle](https://www.luogu.com.cn/problem/P3951), a u dokazu složenosti Shell sorta znatno proširuje teorem $1$.

???+ note "Lema 2"
    Ako su $a,b\ge2$ relativno prosti cijeli brojevi, najveći pozitivan cijeli broj koji nije u skupu $\{ax+by\mid x,y\in \mathbb N \}$ jest $ab-a-b$.

??? note "Dokaz leme 2"
    Dokaz u dva koraka:
    
    -   Najprije dokazujemo da jednadžba $ax+by=ab-a-b$ nema rješenja s nenegativnim cijelim $x,y$:
    
        Bez ograničenja na nenegativnost lako nalazimo dva rješenja $(b-1,-1),(-1,a-1)$.
    
        Iz oblika općeg rješenja $x=x_0+tb,y=y_0-ta$ lako se vidi da su ta dva rješenja „susjedna” (jer je $b-1-b=-1$).
    
        Kad $t$ raste, $x$ raste, a $y$ pada, pa bi se nenegativno cjelobrojno rješenje, ako postoji, moralo nalaziti između ta dva rješenja; no ona su „susjedna” i između njih nema drugih rješenja.
    
        Dakle nenegativnog cjelobrojnog rješenja nema.
    -   Zatim dokazujemo da za svaki cijeli broj $c > ab-a-b$ jednadžba $ax+by=c$ ima nenegativno cjelobrojno rješenje:
    
        Nađimo rješenje $(x_0,y_0)$ s $0\le x_0 < b$ (po obliku općeg rješenja to je moguće).
    
        Tada je:
    
        $$
        by_0=c-ax_0\ge c-a(b-1)>ab-a-b-ab+a=-b
        $$
    
        Dakle $b(y_0+1) > 0$, a kako je $b>0$, slijedi $y_0+1>0$, tj. $y_0\ge 0$.
    
        Stoga je $(x_0,y_0)$ nenegativno cjelobrojno rješenje.
    
    Time je dokaz završen.

Sljedeći teorem pokazuje kako lema $2$ proširuje teorem $1$.

???+ note "Teorem 2"
    Neka su $h_{t+1}>h_t>h_{t-1}$ pozitivni cijeli brojevi. Ako je $\gcd(h_{t+1},h_t)=1$, onda nakon što program izvrši $\text{InsertionSort}(h_{t+1})$ i $\text{InsertionSort}(h_t)$, izvršavanje $\text{InsertionSort}(h_{t-1})$ ima vremensku složenost $O\left(\dfrac{nh_{t+1}h_t}{h_{t-1}} \right)$, a za svaki $j$ broj pomaka pokazivača $i$ je reda $O\left(\dfrac{h_{t+1}h_t}{h_{t-1}} \right)$.

??? note "Dokaz teorema 2"
    U nastavku $A$ označava niz prije poziva $\text{InsertionSort}(h_{t-1})$. Fiksirajmo indeks $j$ vanjske petlje; vrijednost koju umećemo je $v=A_j$.
    
    Za $j\le h_{t+1}h_t$ broj pomaka pokazivača $i$ očito je reda $O\left(\dfrac{h_{t+1}h_t}{h_{t-1}} \right)$.
    
    Stoga u nastavku pretpostavljamo $j>h_{t+1}h_t$.
    
    Za svaki pozitivan cijeli broj $k$ s $1\le k\le j-h_{t+1}h_t$ uočimo: $h_{t+1}h_t-h_{t+1}-h_t<h_{t+1}h_t\le j-k\le j-1$.
    
    Kako je $\gcd(h_{t+1},h_t)=1$, po lemi $2$ postoje nenegativni cijeli brojevi $a,b$ takvi da je $ah_{t+1}+bh_t=j-k$.
    
    Odnosno:
    
    $$
    k=j-ah_{t+1}-bh_t
    $$
    
    Po teoremu $1$ vrijedi:
    
    $$
    A_{j-bh_t}\le A_{j-(b-1)h_t}\le \ldots\le A_{j-h_t}\le A_j
    $$
    
    i
    
    $$
    A_{j-bh_t-ah_{t+1}}\le A_{j-bh_t-(a-1)h_{t+1}}\le \ldots\le A_{j-bh_t-h_{t+1}}\le A_{j-bh_t}
    $$
    
    Zajedno to daje $A_k=A_{j-ah_{t+1}-bh_t}\le A_j$.
    
    Dakle za svaki $1\le k\le j-h_{t+1}h_t$ vrijedi $A_k\le A_j$.
    
    U već obrađenom prefiksu podniza kojem pripada $v$ samo elementi čiji je izvorni indeks u $(j-h_{t+1}h_t,j)$ mogu biti veći od $v$, a takvih je najviše $\left\lceil\dfrac{h_{t+1}h_t}{h_{t-1}}\right\rceil$. Prethodna umetanja sortirala su samo prefiks tog podniza, pa u gornjem pseudokodu $i$ pri svakom koraku pada za $h_{t-1}$ i, čim prijeđe te elemente, naiđe na element koji nije veći od $v$ ili izađe preko lijevog kraja niza, čime petlja while završava. Broj pomaka je $O\left(\dfrac{h_{t+1}h_t}{h_{t-1}} \right)$.
    
    Dokazavši složenost pomaka za svaki $j$, dobivamo ukupnu vremensku složenost:
    
    $$
    \sum_{j=h_{t-1}+1}^n{O\left(\frac{h_{t+1}h_t}{h_{t-1}} \right)}=O\left(\frac{nh_{t+1}h_t}{h_{t-1}}\right)
    $$
    
    Time je dokaz završen.

Pažljivo promatrajući dokaz teorema $2$ uočavamo: teorem 1 dopušta „linearne kombinacije”, tj. ako je $A$ sortiran s razmakom $h$ i sortiran s razmakom $k$, onda je sortiran i s razmakom koji je linearna kombinacija $h$ i $k$ s nenegativnim koeficijentima. Tu „linearnost” jamči upravo lema $2$.

S ta dva teorema možemo dokazati tvrdnje $1$ i $2$.

??? note "Dokaz tvrdnje 1"
    Zapišimo $H$ kao niz:
    
    $$
    H(h_1=1,h_2=3,h_3=7,\ldots,h_{\lfloor \log_2 n\rfloor}=2^{\lfloor \log_2 n\rfloor}-1)
    $$
    
    Shell sort izvršava redom: $\text{InsertionSort}(h_{\lfloor \log_2 n\rfloor}),\text{InsertionSort}(h_{\lfloor \log_2 n\rfloor-1}),\ldots,\text{InsertionSort}(h_2),\text{InsertionSort}(h_1)$.
    
    Neka je $n\ge4$; složenost analiziramo u dva dijela:
    
    -   Za prvih nekoliko razmaka $h_t$ koji zadovoljavaju $h_t\ge \sqrt{n}$ očito je vremenska složenost $\text{InsertionSort}(h_t)$ jednaka $O\left(\dfrac{n^2}{h_t} \right)$.
    
        Uzmimo $k=\min\{t:h_t\ge\sqrt n\}$; tada je $h_k=\Theta(\sqrt n)$ i vrijedi:
    
        $$
        O\left(\frac{n^2}{h_k} \right)=O(n^{3/2})
        $$
    
        A za $h_i$ s $i> k$, budući da je $2h_i< h_{i+1}$, dobivamo:
    
        $$
        O\left(\frac{n^2}{h_i} \right)=O(n^{3/2}/2^{i-k})\,(i>k)
        $$
    
        Dakle ukupna vremenska složenost dijela s razmacima većim ili jednakim $\sqrt n$ iznosi:
    
        $$
        \sum_{i=k}^{\lfloor \log_2 n\rfloor}{O(n^{3/2}/2^{i-k})}=O(n^{3/2})
        $$
    -   Za preostale članove s $h_t< \sqrt{n}$, složenost prvih dvaju i dalje je $O(n^{3/2})$, a za kasnije članove $h_t$ po teoremu $2$ vremenska je složenost:
    
        $$
        O\left(\frac{nh_{t+2}h_{t+1}}{h_t} \right)=O\left(\frac{nh_{t+2}\cdot h_{t+2}/2}{h_{t+2}/4} \right)=O(nh_{t+2})
        $$
    
        Ponovno koristeći svojstvo $2h_i < h_{i+1}$, ukupna vremenska složenost tog dijela je ($k$ u izrazu ima isto značenje kao u prethodnom slučaju):
    
        $$
        2O(n^{3/2})+\sum_{i=1}^{k-3}{O(nh_{i+1})}=O(n^{3/2})+\sum_{i=1}^{k-3}{O(nh_{k-1}/2^{k-i-3})}=O(n^{3/2})+O(nh_{k-1})=O(n^{3/2})
        $$
    
    Ukupna vremenska složenost stoga je $O(n^{3/2})$.

??? note "Dokaz tvrdnje 2"
    Uočimo činjenicu: ako su već izvršeni $\text{InsertionSort}(2)$ i $\text{InsertionSort}(3)$, onda zbog $2\cdot 3-2-3=1$ po teoremu $2$ za svaki element samo neposredno prethodni element može biti veći od njega, a svi raniji elementi su manji. Zato pokazivač $i$ izlazi iz petlje while nakon najviše dva koraka. Drugim riječima, ako se tada izvrši $\text{InsertionSort}(1)$, složenost pada na $O(n)$.
    
    Dalje: ako su već izvršeni $\text{InsertionSort}(4)$ i $\text{InsertionSort}(6)$, promotrimo podniz elemenata s neparnim indeksima i podniz elemenata s parnim indeksima. To odgovara tome da se na ta dva podniza zasebno izvrše $\text{InsertionSort}(2)$ i $\text{InsertionSort}(3)$. Jednako tako, izvršavanje $\text{InsertionSort}(2)$ tada odgovara zasebnom izvršavanju $\text{InsertionSort}(1)$ na dva podniza, pa je potrebno samo vrijeme reda zbroja duljina dvaju nizova, tj. $O(n)$, da niz postane sortiran s razmakom $2$.
    
    Induktivnim nastavkom dobivamo: ako su već izvršeni $\text{InsertionSort}(2h)$ i $\text{InsertionSort}(3h)$, složenost izvršavanja $\text{InsertionSort}(h)$ također je samo $O(n)$.
    
    Složenost zatim analiziramo u dva dijela:
    
    -   Za dio s $h_t>n/3$ složenost izvršavanja svakog $\text{InsertionSort}(h_t)$ je $O(n^2/h_t)$.
    
        Kako je $n^2/h_t<3n$, složenost jednog insertion sorta je $O(n)$.
    
        Broj takvih članova je reda $O(\log^2 n)$, pa je vremenska složenost tog dijela $O(n\log^2 n)$.
    -   Za dio s $h_t\le n/3$, budući da je $3h_t\le n$, prije toga su već izvršeni $\text{InsertionSort}(2h_t)$ i $\text{InsertionSort}(3h_t)$, pa je vremenska složenost izvršavanja $\text{InsertionSort}(h_t)$ jednaka $O(n)$.
    
        Jednako tako, broj članova u tom dijelu je reda $O(\log^2 n)$, pa je vremenska složenost tog dijela $O(n\log^2 n)$.
    
    Ukupna vremenska složenost stoga je $O(n\log^2 n)$.

### Prostorna složenost

Prostorna složenost Shell sorta je $O(1)$.

## Implementacija

=== "C++[^ref1]"
    ```cpp
    template <typename T>
    void shell_sort(T array[], int length) {
      int h = 1;
      while (h < length / 3) {
        h = 3 * h + 1;
      }
      while (h >= 1) {
        for (int i = h; i < length; i++) {
          for (int j = i; j >= h && array[j] < array[j - h]; j -= h) {
            std::swap(array[j], array[j - h]);
          }
        }
        h = h / 3;
      }
    }
    ```

=== "Python"
    ```python
    def shell_sort(array, length):
        h = 1
        while h < length / 3:
            h = int(3 * h + 1)
        while h >= 1:
            for i in range(h, length):
                j = i
                while j >= h and array[j] < array[j - h]:
                    array[j], array[j - h] = array[j - h], array[j]
                    j -= h
            h = int(h / 3)
    ```

## Literatura i bilješke

[^ref1]: [Shellsort – Wikipedia](https://en.wikipedia.org/wiki/Shellsort)
