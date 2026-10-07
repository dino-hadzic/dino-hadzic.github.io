---
title: Rotating calipers
---

Ova stranica uglavnom predstavlja metodu rotating calipers (rotirajuće pomično mjerilo).

## Uvod

Algoritam rotating calipers (rotirajuće pomično mjerilo, u kineskoj literaturi „旋转卡壳”), nadograđujući se na algoritam za konveksnu ljusku, nabraja stranice ljuske i istodobno održava ostale potrebne točke, pa u linearnom vremenu rješava probleme vezane uz svojstva konveksne ljuske, kao što su promjer ljuske ili najmanji pokrivajući pravokutnik.

???+ note "Kineski naziv algoritma"
    Uobičajeni kineski naziv ovog algoritma je „旋转卡壳” (xuánzhuǎn qiǎké, otprilike „rotirajuće zaglavljivanje”). Može se shvatiti ovako: za stranicu koju trenutno nabrajamo, kroz svaku održavanu točku možemo povući pravac paralelan s njom ili okomit na nju; da bismo osigurali optimalnost za trenutnu stranicu, zadatak nam je da ti pravci ljusku točno „zaglave” (stegnu). Stranice se obično nabrajaju redom kojim se zakreću u nekom smjeru, pa se cijeli postupak sastoji od „rotiranja” i „zaglavljivanja”.
    
    Doslovan prijevod engleskog naziva „rotating calipers” bio bi „rotirajuće pomično mjerilo”, pri čemu „calipers” znači „pomično mjerilo (šubler)”. Izvorna zamisao rada koji je prvi uveo taj naziv[^ref1]: podesivim „pomičnim mjerilom” stegnemo konveksnu ljusku, a zatim ga „rotiramo” oko ljuske.

## Promjer konveksne ljuske

???+ note "Primjer 1: [Luogu P1452 Beauty Contest G](https://www.luogu.com.cn/problem/P1452)"
    Zadano je $n$ točaka u ravnini; treba naći najveću udaljenost među svim parovima točaka. ($2\leq n \leq 50000,|x|,|y| \leq 10^4$)

### Postupak

Najprije bilo kojim algoritmom za konveksnu ljusku izračunamo ljusku zadanih točaka; par točaka s najvećom udaljenošću sigurno je na ljusci. Zbog oblika ljuske primjećujemo: ako stranice ljuske obilazimo u smjeru suprotnom od kazaljke na satu i za svaku stranicu nađemo njoj najudaljeniju točku, onda se, kako se stranica zakreće, i odgovarajuća najudaljenija točka zakreće u smjeru suprotnom od kazaljke na satu, nikad u suprotnom smjeru. To znači da pri nabrajanju stranica ljuske u smjeru suprotnom od kazaljke na satu možemo pamtiti i održavati trenutnu najudaljeniju točku te stalno računati i ažurirati odgovor.

Polje dobiveno nakon računanja ljuske prirodno je poredano u smjeru suprotnom od kazaljke na satu, ali ne zaboravite unaprijed dodati čvor 1 (najdonji lijevi) na kraj polja, kako bismo pri nabrajanju stranica $(i,i+1)$ redom obišli sve stranice.

![](images/rotating-calipers1.png)

Tijekom nabrajanja za svaku stranicu provjeravamo je li udaljenost točke $j+1$ od stranice $(i,i+1)$ veća od udaljenosti točke $j$; ako jest, povećamo $j$ za jedan, a inače je $j$ optimalna točka za tu stranicu. Udaljenosti točaka od stranice uspoređujemo tako da vektorskim produktom izračunamo površine dvaju trokuta (kao na slici, žuti i plavi trokut imaju zajedničku osnovicu) i izravno ih usporedimo.

### Implementacija

???+ note "Ključni dio koda"
    === "C++"
        ```cpp
        int sta[N], top;  // indekse čvorova na ljusci čuvamo na stogu; prvi i posljednji čvor imaju isti indeks
        
        ll pf(ll x) { return x * x; }
        
        ll dis(int p, int q) { return pf(a[p].x - a[q].x) + pf(a[p].y - a[q].y); }
        
        ll sqr(int p, int q, int y) { return abs((a[q] - a[p]) * (a[y] - a[q])); }
        
        ll mx;
        
        void get_longest() {  // promjer konveksne ljuske
          int j = 3;
          if (top < 4) {
            mx = dis(sta[1], sta[2]);
            return;
          }
          for (int i = 1; i < top; ++i) {
            while (sqr(sta[i], sta[i + 1], sta[j]) <=
                   sqr(sta[i], sta[i + 1], sta[j % top + 1]))
              j = j % top + 1;
            mx = max(mx, max(dis(sta[i + 1], sta[j]), dis(sta[i], sta[j])));
          }
        }
        ```
    
    === "Python"
        ```python
        sta = [0] * N
        top = 0  # indekse čvorova na ljusci čuvamo na stogu; prvi i posljednji čvor imaju isti indeks
        
        
        def pf(x):
            return x * x
        
        
        def dis(p, q):
            return pf(a[p].x - a[q].x) + pf(a[p].y - a[q].y)
        
        
        def sqr(p, q, y):
            return abs((a[q] - a[p]) * (a[y] - a[q]))
        
        
        def get_longest():  # promjer konveksne ljuske
            j = 3
            if top < 4:
                mx = dis(sta[1], sta[2])
                return
            for i in range(1, top):
                while sqr(sta[i], sta[i + 1], sta[j]) <= sqr(
                    sta[i], sta[i + 1], sta[j % top + 1]
                ):
                    j = j % top + 1
                mx = max(mx, max(dis(sta[i + 1], sta[j]), dis(sta[i], sta[j])))
        ```

## Najmanji pokrivajući pravokutnik

[Luogu P3187 Najmanji pokrivajući pravokutnik](https://www.luogu.com.cn/problem/P3187)

Zadane su koordinate nekih točaka; treba naći pravokutnik najmanje površine koji pokriva sve točke. ($3\leq n \leq 50000$)

### Postupak

Nakon prethodnog zadatka kao uvoda, i ovdje se prirodno nameće metoda rotating calipers, ali sada se traži površina. Ako bismo, kao u prethodnom zadatku, održavali samo jednu optimalnu točku, našli bismo samo par paralelnih pravaca na najmanjoj udaljenosti; trebamo još odrediti lijevu i desnu granicu pravokutnika. Zato ovaj put održavamo tri točke: jednu nasuprot pravcu koji nabrajamo i dvije na različitim bočnim stranama. Optimalnu točku nasuprot i dalje određujemo uspoređujući površine izračunane vektorskim produktom; usporedba površina ovdje je zapravo usporedba jedne stranice pravokutnika. Optimalne bočne točke određujemo skalarnim produktom, jer usporedba skalarnih produkata znači usporedbu duljina projekcija, a zbroj lijeve i desne projekcije predstavlja drugu stranicu pravokutnika. Optimalnosti tih dviju stranica međusobno su neovisne, pa, kad nađemo položaje triju optimalnih točaka, možemo odrediti najmanju površinu pravokutnika koji pokriva sve točke i kojem je pravac trenutne stranice jedna od stranica.

![](images/rotating-calipers2.png)

Pri konačnom računanju odgovora, ako zadatak ne traži sva četiri vrha, postoji prilično domišljat način da se površina pravokutnika izračuna izravno pomoću vektorskog i skalarnog produkta. Neka je $S$ dvostruka površina ljubičastog dijela; konačna površina je

$$
S\times (|\overrightarrow{AD}\cdot \overrightarrow{AB}|+|\overrightarrow{BC}\cdot \overrightarrow{BA}|-|\overrightarrow{AB}\cdot \overrightarrow{BA}|)/|\overrightarrow{AB}\cdot \overrightarrow{BA}|
$$

### Implementacija

Nužno računanje konveksne ljuske je izostavljeno; ovdje je ključni dio koda za ovaj zadatak:

???+ note "Ključni dio koda"
    === "C++"
        ```cpp
        void get_biggest() {
          int j = 3, l = 2, r = 2;
          double t1, t2, t3, ans = 2e10;
          for (int i = 1; i < top; ++i) {
            while (sqr(sta[i], sta[i + 1], sta[j]) <=
                   sqr(sta[i], sta[i + 1], sta[j % top + 1]))
              j = j % top + 1;
            while (dot(sta[i + 1], sta[r % top + 1], sta[i]) >=
                   dot(sta[i + 1], sta[r], sta[i]))
              r = r % top + 1;
            if (i == 1) l = r;
            while (dot(sta[i + 1], sta[l % top + 1], sta[i]) <=
                   dot(sta[i + 1], sta[l], sta[i]))
              l = l % top + 1;
            t1 = sqr(sta[i], sta[i + 1], sta[j]);
            t2 = dot(sta[i + 1], sta[r], sta[i]) + dot(sta[i + 1], sta[l], sta[i]);
            t3 = dot(sta[i + 1], sta[i + 1], sta[i]);
            ans = min(ans, t1 * t2 / t3);
          }
        }
        ```
    
    === "Python"
        ```python
        def get_biggest():
            j = 3
            l = 2
            r = 2
            ans = 2e10
            for i in range(1, top):
                while sqr(sta[i], sta[i + 1], sta[j]) <= sqr(
                    sta[i], sta[i + 1], sta[j % top + 1]
                ):
                    j = j % top + 1
                while dot(sta[i + 1], sta[r % top + 1], sta[i]) >= dot(
                    sta[i + 1], sta[r], sta[i]
                ):
                    r = r % top + 1
                if i == 1:
                    l = r
                while dot(sta[i + 1], sta[l % top + 1], sta[i]) <= dot(
                    sta[i + 1], sta[l], sta[i]
                ):
                    l = l % top + 1
                t1 = sqr(sta[i], sta[i + 1], sta[j])
                t2 = dot(sta[i + 1], sta[r], sta[i]) + dot(sta[i + 1], sta[l], sta[i])
                t3 = dot(sta[i + 1], sta[i + 1], sta[i])
                ans = min(ans, t1 * t2 / t3)
        ```

## Zadaci za vježbu

-   [POJ 3608. Bridge Across Islands](http://poj.org/problem?id=3608)
-   [2011 ACM-ICPC World Finals, Problem K. Trash Removal](https://codeforces.com/gym/101175)
-   [ICPC WF Moscow Invitational Contest - Online Mirror, Problem F. Framing Pictures](https://codeforces.com/contest/1578/problem/F)

## Literatura i napomene

[^ref1]: Toussaint, Godfried T. (1983). "Solving geometric problems with the rotating calipers". Proc. MELECON '83, Athens. CiteSeerX 10.1.1.155.5671

-   <https://en.wikipedia.org/wiki/Rotating_calipers>

-   <http://www-cgrl.cs.mcgill.ca/~godfried/research/calipers.html>

-   Shamos, Michael (1978). "Computational Geometry" (PDF). Yale University. pp. 76–81.
